from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return self.caption

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateField() # Automatically set whenever there is an update
    slug = models.SlugField(max_length=100, unique=True, default="", db_index=True) # Unique True implies an index
    content = models.TextField(validators=[MinLengthValidator(10)])
    url_link = models.URLField(max_length = 400)
    tag = models.ManyToManyField(Tag, null=False, related_name="projects")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.title}"