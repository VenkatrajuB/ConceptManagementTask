from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    loc=forms.CharField(max_length=20)
    mail = forms.EmailField(max_length=50)