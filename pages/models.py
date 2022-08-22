from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=50)
    img = models.ImageField(upload_to='photos')
    facebookLK = models.URLField(null=True, blank=True, max_length=255)
    twitterLK = models.URLField(null=True, blank=True, max_length=255)
    googlePlusLK = models.URLField(null=True, blank=True, max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    @mark_safe
    def icone(self):
        return f'<img width="35px" src="/media/{self.img}"'

    def __str__(self):
        return self.name

