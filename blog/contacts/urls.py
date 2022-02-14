from django.urls import path
from contacts.views import ContactUsView

urlpatterns = [
    path("contact/", ContactUsView.as_view(), name="contact_us")
]


