from django import forms

class Registration(forms.Form):
    fname=forms.CharField()
    lname=forms.CharField()
    email=forms.EmailField()
    city=forms.CharField()