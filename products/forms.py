from django import forms
from .models import Review, Product, ProductImage
from haystack.forms import SearchForm



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'inventory']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']