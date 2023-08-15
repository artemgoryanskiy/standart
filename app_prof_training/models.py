from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class CategoryProfTrain(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='category_img/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProgramProfTrain(models.Model):
    code_num = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    class_num = models.CharField(max_length=10)
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


