from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from app_prof_dev.models import CategoryProfDev


class Tutor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    education = models.TextField()
    photo = models.ImageField(upload_to='tutors/', blank=True, null=True)
    description = models.TextField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    vk_link = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    rate = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,
                               validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    class Meta:
        ordering = ['last_name']


class BecomeTutor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    education = models.TextField()
    work_experience = models.IntegerField()
    phone = models.CharField(max_length=16)
    email = models.EmailField()