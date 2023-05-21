from cProfile import label
from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title","subtitle","phone","email_adress","content",)
        labels = {"title":"Введите имя","subtitle":"Введите фамилию","phone":"Введите телефон","email_adress":"Ваш email","content":"Напишите о себе"}