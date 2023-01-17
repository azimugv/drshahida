from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    show_on_home = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    img = models.ImageField(upload_to='featured_image')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class SerialNumber(models.Model):
    serial_num = PhoneNumberField(blank=True)
    

    def __str__(self):
        return self.serial_num
