from django import forms
from calculate.models import UserProfile,Myindex,Expectedindex,CourseCode,IndexNumber,Email
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class MyIndexForm(forms.ModelForm):
    index = forms.CharField(max_length=100, help_text="Please enter your index.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Myindex
        fields = ('index','views')


class ExpectedIndexForm(forms.ModelForm):
    expectedindex = forms.CharField(max_length=100, help_text="Please enter the index you want.")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model = Expectedindex
        fields = ('expectedindex','views')

class CourseForm(forms.ModelForm):
    code = forms.CharField(max_length=50,help_text="Please enter a Course code.")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model = CourseCode
        fields = ('code','views')

class IndexForm(forms.ModelForm):
    index = forms.IntegerField(initial=0,help_text="Please enter a index.")
    post = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model = IndexNumber
        fields = ('index','post')


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    class Meta:
        model= Email
        fields = ('name','email','message')