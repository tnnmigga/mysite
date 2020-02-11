from django.db import models

# Create your models here.

class Gallery(models.Model):
    """Model definition for Gallery."""
    description = models.CharField(default='在这里填作品简介',max_length=100)
    image = models.ImageField(default='default.png', upload_to='image/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(default='作品标题', max_length=50)

    def __str__(self):
        return self.title
