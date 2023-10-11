from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField


class CategoryProfTrain(models.Model):
    title = models.CharField(max_length=300)
    short_desc = models.TextField(null=True, blank=True)
    audience_category = models.TextField(null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='prof_train/category_img/', blank=True, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,
                               validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.title

    def get_class_name(self):
        return self.__class__.__name__

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProgramProfTrain(models.Model):
    DOCUMENTS = (
        ('certificate', 'Свидетельство об обучении'),
        ('book', 'Удостоверение'),
    )
    code_num = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    class_num = models.CharField(max_length=50)
    document = MultiSelectField(max_length=200, blank=True, null=True, choices=DOCUMENTS)
    hours = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(null=False, max_length=100)
    category = models.ForeignKey(CategoryProfTrain, on_delete=models.CASCADE, default=1, related_name='programs')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_class_name(self):
        return self.__class__.__name__
