from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username','email', 'password']
        widgets = {'password':forms.PasswordInput}
        lebels ={
            'Email Address':'Email'
        }
        help_texts = {'username':''}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['title','content','contact','profile_Picture']
        
             
class Blog_userForm(forms.ModelForm):
    class Meta:
        model = Blog_user
        fields = '__all__'