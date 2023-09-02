from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'published_date')

    # Agrega clases de Bootstrap a los widgets
    widgets = {
        'author': forms.Select(),
        'title': forms.TextInput(),
        'text': forms.Textarea(attrs={'class': 'form-control'}),
        'published_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
    }
