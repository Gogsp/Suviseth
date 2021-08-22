from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields, formsets, widgets
from django.forms.forms import Form
from SuvisethApp.models import Admin, Category, ServiceProvider, Customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Email Id'}),
        }

class ClientForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('profile_pic','first_name','last_name','date_of_birth','mobile_no','address','district')

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control','placeholder':'MM/DD/YYYY'}),
            'mobile_no': forms.TextInput(attrs={'class':'form-control','placeholder':'07xxxxxxxx'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'district': forms.Select(attrs={'class':'form-control'})
        }
        
        

class ServiceProviderForm(forms.ModelForm):
    class Meta():
        model = ServiceProvider
        fields = ('company_logo','company_name','mobile_no','district')

        widgets = {
            'company_logo': forms.FileInput(attrs={'class':'form-control'}),
            'company_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'mobile_no': forms.TextInput(attrs={'class':'form-control','placeholder':'07xxxxxxxx'}),
            'district': forms.Select(attrs={'class':'form-control'})
        }

class AdminForm(forms.ModelForm):
    class Meta():
        model = Admin
        fields = ('profile_pic',)

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ('name','description','images')
    
    widgets = {
        'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Service Name'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'images': forms.FileInput(attrs={'class':'form-control'}),
    }
        

    