from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    original_url = models.URLField()
    shortcode = models.CharField(max_length=20,unique=True,null=True,blank=True)
    clicks = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.shortcode) 