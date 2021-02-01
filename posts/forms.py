from django import forms
from .models import Post
from django.forms import Textarea


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']

        widgets = {

            "text": Textarea(attrs={
                 "placeholder": "Введите текст записи",
            }),

        }

        def clean_text(self):
            text = forms.cleaned_data['text']
            if text == '':
                raise forms.ValidationError("Заполни это поле!",
                                            params={"text": text})
            return text
