from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class ProductLabProt(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=False)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='labor_prot_img/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
