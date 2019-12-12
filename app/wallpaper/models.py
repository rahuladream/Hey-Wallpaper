from django.db import models
from PIL import Image
from io import BytesIO
import os
from django.core.files.base import ContentFile
THUMB_SIZE = (70, 70)
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True)
    image = models.ImageField(upload_to='category/%Y/%d', help_text="Please make sure the image size should be 400 * 200")

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return f"category/{self.slug}"
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True)

    def get_absolute_url(self):
        return f"/tag/{self.name}"
    
    def __str__(self):
        return self.name

class Wallpaper(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Wallpaper Categories')
    image = models.ImageField(upload_to='wallpapers/%Y/%d')
    thumbnail = models.ImageField(upload_to='thumbs/%Y/%d', editable=False)
    tags = models.ManyToManyField(Tag)
    rate_avg = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_views = models.IntegerField(default=0)
    total_download = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)   

    def save(self, *args, **kwargs):
    
        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Wallpaper, self).save(*args, **kwargs)

    def make_thumbnail(self):

        image = Image.open(self.image)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)
class Rating(models.Model):
    post_id = models.ForeignKey(Wallpaper, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    rate = models.IntegerField(choices=Rating_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post_id)