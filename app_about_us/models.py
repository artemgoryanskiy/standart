from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents/')


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
