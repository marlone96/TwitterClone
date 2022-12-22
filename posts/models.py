from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class meta(object):
        db_table = 'post'
    
    #handle= models.CharField(
    #    'handle', blank=False, null=False,max_length=14, db_index=True, default='@anon'
    #)

    name= models.CharField(
        'name', blank=False, null=False,max_length=14, db_index=True, default='Anonymous'
    )
    body= models.CharField(
        'Body',blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'created_at', blank=True, auto_now_add=True
    )

    image=CloudinaryField(
        'image', blank = True, db_index=True
    )
    likes=models.PositiveIntegerField(
        'likes', default=0, blank=True

    )

    def __str__(self):
        return self.name
