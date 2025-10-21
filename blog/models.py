from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='Admin')
    slug = models.SlugField(unique=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # REFINEMENT: Only generate slug if it doesn't exist
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            # CRITICAL FIX: Loop to ensure slug is always unique
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    content = models.TextField()
    

    
