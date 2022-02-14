from django import forms
from contacts.models import Contact


class ContactUsForm(forms.Form):
    """
    Contact_Us Form
    """
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-2",
        "placeholder": "Enter your name...",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control mb-2",
        "placeholder": "Enter your email...",
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-2",
        "placeholder": "Enter message subject...",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control mb-2",
        "placeholder": "Enter your message...",
    }))

    def save(self):
        """
        get fields values and create a Contact Model instance
        """
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]

        # Create Contact-Us instance
        contact_instance = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        contact = contact_instance.save()
        return contact
