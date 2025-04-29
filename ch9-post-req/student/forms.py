from django import forms

class Registration(forms.Form):
    name=forms.CharField(max_length=70)
    email=forms.EmailField(max_length=250)
    city=forms.CharField(max_length=75)
    contact=forms.IntegerField()
    