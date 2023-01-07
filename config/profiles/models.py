from django.db import models
from django.contrib.auth.models import AbstractUser

class UserNet(AbstractUser):
    """Custom user model"""

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    email = models.EmailField("email address", unique=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField('General information', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    birthday = models.DateField(blank=True, null=True)
    technology = models.ManyToManyField('Technology', related_name='users')

class Technology(models.Model):
    """
    Technology model
    """
    name = models.CharField('technology', max_length=128)


    def __str__(self):
        return self.name
