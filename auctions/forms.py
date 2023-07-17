from django import forms
from .models import Category




class NewListing(forms.Form):
    title = forms.CharField(label="Title",widget=forms.TextInput(attrs={
        'placeholder': 'Name', 
        'style': 'width: 300px;', 
        'class': 'form-control'
        }))

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())


    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Please enter the  description',
        'class': 'form-control',

        }))
    
    url = forms.URLField(label="Link to Image", required=False, widget=forms.TextInput(attrs={
         'class': 'form-control',
         'style': 'width: 300px;', 
    }))
    starting_price = forms.DecimalField(max_digits=14, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'style': 'width: 300px;', 
    }))



class Watchlist(forms.Form):
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}),required=False, label="Add to Watchlist?")