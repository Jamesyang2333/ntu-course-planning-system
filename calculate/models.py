from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Myindex(models.Model):
    index = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.index


class Expectedindex(models.Model):
    myindex = models.ManyToManyField(Myindex)
    expectedindex = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.expectedindex


class CourseCode(models.Model):
    code = models.CharField(max_length=50,unique=True)
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.code

class IndexNumber(models.Model):
    course = models.ForeignKey(CourseCode,null=True,on_delete=models.SET_NULL)
    index = models.IntegerField(default=0)
    post = models.IntegerField(default=0)
    def __unicode__(self):
        return self.index


class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message= models.CharField(max_length=100000)
    def __unicode__(self):
        return self.name
