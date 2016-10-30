from django.forms import forms, fields


ISSUES = [("Economy", "Economy"), ("Health Care", "Health Care"),
          ("Terrorism", "Terrorism"), ("Environment", "Environment"), ]


class IssueForm(forms.Form):
    issue = fields.ChoiceField(choices=ISSUES)
