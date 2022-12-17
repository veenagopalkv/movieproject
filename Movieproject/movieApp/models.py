from django.db import models

# Create your models here.
class movie(models.Model):
       name=models.CharField(max_length=256)
       description=models.TextField()
       year=models.IntegerField()
       image=models.ImageField(upload_to="pics")

       def __str__(self):
           return self.name