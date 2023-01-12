from .models import News, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['category', 'title', 'anons', 'date', 'full_text']
        choice_category = News.category

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),

            "category": Select(attrs={
                'category': News.category,
                'class': 'form-control',
                'placeholder': 'Категория статьи'
            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text', )