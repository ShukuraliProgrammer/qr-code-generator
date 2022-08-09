from .models import Template, QrCode
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class GenerateQRForm(forms.ModelForm):
    class Meta:
        model = QrCode
        fields = [
            'name', 'url',
            'scale',
            'color'
        ]








class TemplateForm(forms.ModelForm):

    class Meta:
        model = Template
        fields = (
            'qrname','color_primary','color_button','user', 'scale',
            'color','image', 'headline','social_media_type' ,'title1',
            'url1','social_media_type2','title2', 'url2','social_media_type3', 
            'title3', 'url3',
         )


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
