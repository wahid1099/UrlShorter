from django.db import models

# Create your models here.

class ShortURL(models.Model):
    orginal_url = models.URLField(max_length=700,null=True,blank=True)
    short_url = models.CharField(max_length=255,null=True, blank=True)
    time_date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.orginal_url