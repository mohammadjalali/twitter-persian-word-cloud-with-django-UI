from django.db import models
class Config(models.Model):

    username = models.CharField(max_length=200, default='1mohammadjalali'),
    image = models.ImageField(default='templates/twitter-logo.jpg'),
        
    def __str__(self):
        return self.username


# Create your models here.
