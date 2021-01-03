from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(max_length=300, null=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title