from django.db import models

# Create your models here.

class Skills(models.Model):
    skills=models.CharField(max_length=100)

class Sample(models.Model):
    name=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    skills=models.ForeignKey(Skills, on_delete=models.CASCADE,related_name="talent")
    attachment = models.FileField()

