from django.db import models
from django.utils.text import slugify

class Blog(models.Model):
    def __str__(self):
        return f"{self.title}"

    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50, null=True)
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
# ...com/Category/category-name
class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=155)
    #slug = models.SlugField(null=True, unique=True, db_index=True, editable=False, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
