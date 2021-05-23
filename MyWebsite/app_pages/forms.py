from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=25)
    email = forms.EmailField()
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea)
