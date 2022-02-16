from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


def cover_uploader(instance, filename):
    filename = f'{instance.title[:15]}-Cover.png'
    return f'articles/{filename}'


class Writer(models.Model):
    """
    Writer model [ONLY WRITERS CAN EDIT OR CREATE ARTICLE]
    """
    user 					= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 


class Article(models.Model):
    """
    Articles Model
    """
    title 					= models.CharField(max_length=150)
    text 					= RichTextField()
    cover 					= models.ImageField(upload_to=cover_uploader, blank=True, null=True)
    writer 					= models.ForeignKey(Writer, on_delete=models.CASCADE)
    timestamp 				= models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"pk": self.id, "slug": slugify(self.title)})

    class Meta:
        """
        order articles by id --> last to first
        """
        ordering = ["-id"]

