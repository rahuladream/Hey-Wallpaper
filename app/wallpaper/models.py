from django.db import models

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
    

class Tag(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True)

    def get_absolute_url(self):
        return f"/tag/{self.name}"
    
    def __str__(self):
        return self.name
    