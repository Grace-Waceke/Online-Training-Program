from dataclasses import fields
from pyexpat import model
from dataclasses import fields
from pyexpat import model

from django import forms
from. models import Community
class Community_registration_form(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"
        Widgets = {}