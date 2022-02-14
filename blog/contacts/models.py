from django.db import models

class Contact(models.Model):
    """
    Contact-Us Model
    """
    name                    = models.CharField(max_length=60)
    email                   = models.EmailField()
    subject                 = models.CharField(max_length=150)
    message                    = models.TextField()

    def __str__(self):
        return self.subject

