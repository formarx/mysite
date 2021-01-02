from django.db import models

# Create your models here.

class History(models.Model):
    history_text = models.CharField(max_length=100)
    history_date = models.DateField()
    
    def __str__(self):
        return self.history_text

