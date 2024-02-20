from django import forms

from app1.models import movies1

class moviesForm(forms.ModelForm):
    class Meta:
        model=movies1
        fields="__all__"
        
 