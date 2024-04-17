from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    contact = models.IntegerField()
    email = models.EmailField()
    profile_Picture = models.ImageField(upload_to='imgs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Topic(models.Model):
    topic_id = models.OneToOneField(UserProfile,on_delete =models.CASCADE)
    title = models.CharField(max_length = 20)
    topic_qs = models.TextField()
    topic_ans = models.TextField()
    def __str__(self):
        return self.title
    
'''
class Division(models.Model):
    subject_id = models.OneToOneField(UserProfile, on_delete = models.CASCADE)
    subject_name = models.CharField(max_length = 20, primary_key = True)
    subject_desc = models.TextField()
    def __str__(self):
        return self.subject_name 

class Topic(models.Model):
    topic_id = models.OneToOneField(Division, on_delete = models.CASCADE)
    topic_title = models.CharField(max_length = 50)
    topic_query = models.TextField()
    def get_absolute_url(self):
        return reverse('detail',kwargs = {'pk':self.pk})
    def __str__(self):
        return (self.topic_id)
'''
class Blog_user(models.Model):
    Blog_User_Id= models.IntegerField(primary_key = True)
    User_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 8)
    Email_ID = models.EmailField()
    contc_no = models.IntegerField(null = True)
    BirthDate = models.DateField(null = True)
    Picture = models.ImageField(upload_to = 'user_pics')
    def __str__(self):
        return self.User_name

class Blog_post(models.Model):
    User_id = models.ForeignKey(Blog_user, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.User_id)

class Student(models.Model):
    sid = models.IntegerField()
    