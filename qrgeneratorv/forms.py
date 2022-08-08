from .models import Template
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
class TemplateForm(forms.ModelForm):

    class Meta:
        model = Template
        fields = (
            'qrname','color_primary','color_button',
            'image', 'headline','social_media_type' ,'title1',
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

