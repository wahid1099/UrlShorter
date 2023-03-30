from .models import ShortURL
from django import forms


class CreateNewShortUrl(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = {'orginal_url'}
        widgets = {
            'orginal_url': forms.TextInput(attrs={'class': 'form-control'})
        }
