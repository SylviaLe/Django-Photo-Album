from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('cate', args=[str(self.id)])

class Photo(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(
        Category,
        on_delete=SET_NULL, #dont remove the photos when the category is delete
        related_name='photos',
        null=True, #this goes with the SET_NULL above
    )
    image = models.ImageField(null=False, blank=False)  #must install pillow before using this fields

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo', args=[str(self.id)])


