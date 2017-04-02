from django import forms
from .models import  category
from django.forms import ModelForm

class addexpense(forms.Form):
    
    cat=forms.ModelChoiceField(queryset=category.objects.all().order_by('value'))
    Amount=forms.IntegerField()
    Decription=forms.CharField(widget=forms.Textarea())
    
class addcat(ModelForm):
    value=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"New Category"}))
    class Meta:
        model=category
        fields=['value',]