from django.db import models

# Create your models here.
class Problem(models.Model):
    question = models.CharField(max_length=100)
    answer = models.DecimalField(max_digits=5, decimal_places=2)
    