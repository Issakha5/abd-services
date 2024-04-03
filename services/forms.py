from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nom",widget=forms.TextInput(attrs={"class": "form-control","placeholder":""}))
    subject = forms.CharField(
        label="Objet",widget=forms.TextInput(attrs={"class": "form-control","placeholder":""}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control","placeholder":""}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class": "form-control","placeholder":""}))
