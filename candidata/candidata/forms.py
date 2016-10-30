from django import forms
from django.forms import fields
from django.forms.widgets import Select


ISSUES = [("Economy", "Economy"), ("Health Care", "Health Care"),
          ("Terrorism", "Terrorism"), ("Environment", "Environment"), ]


class IssueForm(forms.Form):
    issue = fields.ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=ISSUES)
