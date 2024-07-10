from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=128)
    image = models.CharField(max_length=255, blank=True, null=True)
    intro = models.TextField(blank=True)
    content = models.TextField(blank=True, null=True)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return f"Titre: {self.title}, Auteur:{self.author}"

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug":self.slug})

    class Meta:
        ordering = ['-dateCreated']


