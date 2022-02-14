from django.shortcuts import redirect
from django.views.generic import FormView

from contacts.forms import ContactUsForm


class ContactUsView(FormView):
    """
    Contact-Us View
    """
    form_class = ContactUsForm
    template_name = "contact.html"

    def form_valid(self, form):
        """
        if Form is valid --> Save Form and Create an Instance of Contact Model
        """
        form.save()  # Create a Contact Model Instance
        return redirect("contact_us")  # redirect to previous page (Contact-Us Page)
