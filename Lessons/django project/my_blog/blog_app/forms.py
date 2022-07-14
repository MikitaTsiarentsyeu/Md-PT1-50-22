from dataclasses import field
from pyexpat import model
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label='Title')
    subtitle = forms.CharField(max_length=200, label='Subtitle')
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"content_field"}), label='Content')
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label="Type")
    image = forms.ImageField(label="Hero image")

    def clean_subtitle(self):
        title_data = self.cleaned_data['title']
        subtitle_data = self.cleaned_data['subtitle']

        if subtitle_data == title_data:
            raise ValidationError("The subtitle shold not be the same as the title!")
        
        return subtitle_data

class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')
        labels = {'image':"Hero image"}