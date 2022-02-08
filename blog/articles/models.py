from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


def cover_uploader(instance, filename):
	filename = f'{instance.title[:15]}-Cover.png'
	return f'articles/{filename}'


class Article(models.Model):
	title 					= models.CharField(max_length=150)
	text 					= RichTextField()
	cover 					= models.ImageField(upload_to=cover_uploader, blank=True, null=True)
	writer 					= models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title
