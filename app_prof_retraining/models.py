from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class CategoryProfRetrain(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    short_desc = models.TextField(null=True, blank=True)
    audience_category = models.TextField(null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to='prof_retr/category_img/', blank=True, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,
                               validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProgramProfRetrain(models.Model):
    category = models.ForeignKey(CategoryProfRetrain, related_name='programs', on_delete=models.CASCADE,
                                 verbose_name='Выберите категорию')
    title = models.CharField(max_length=500)
    slug = models.SlugField(null=True, max_length=100)
    hours = models.IntegerField()
    qualification = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
