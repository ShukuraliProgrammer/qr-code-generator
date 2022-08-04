from .models import Template

from django import forms

class TemplateForm(forms.ModelForm):

    class Meta:
        model = Template
        fields = (
            'qrname','color_primary','color_button',
            'image', 'headline','social_media_type' ,'title1',
            'url1','social_media_type2','title2', 'url2','social_media_type3', 
            'title3', 'url3', 'about_us','add_more', 'welcome_screen'
         )
