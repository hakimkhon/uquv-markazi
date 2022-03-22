from django import forms
class LeadForm(forms.Form):
    ism = forms.CharField(max_length=15)
    famila = forms.CharField(max_length=15)
    yosh = forms.IntegerField(min_value=8)

