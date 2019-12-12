from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
THUMB_SIZE = 320
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return f"category/{self.slug}"
    
    def __str__(self):
        return self.name

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


class Tag(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True)

    def get_absolute_url(self):
        return f"/tag/{self.name}"
    
    def __str__(self):
        return self.name

class Wallpaper(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Wallpaper Categories')
    image = models.ImageField(upload_to='wallpaper')
    thumbnail = models.ImageField(upload_to='thumbs', editable=False)
    tags = models.ManyToManyField(Tag)
    total_rate = models.ForeignKey(Rating, on_delete=models.CASCADE)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Creating thumbnail of the image using Pillow
        """
        if not self.make_thumbnail():
            "Set to a default thumbnail"
            raise Exception('Could not create thumbnail - is the file type valid')
        super(Wallpaper, self).save(*args, **kwargs)

    def make_thumbnail(self):
        """
        Real work of creating thumbnail
        """
        image = Image.open(self.image)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splittext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False # Unknown filetype

        "Save thumbnail to in-memory file as StringIO"
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        #set save = False, otherwise it will run in the infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True