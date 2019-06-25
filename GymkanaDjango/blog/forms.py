from django import forms

from blog.models import New


class NewsForm(forms.ModelForm):
    class Meta:
        model = New

        fields = [
            'title',
            'subtitle',
            'body',
            'image',
        ]
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'body': 'Noticia',
            'image': 'Imagen',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

