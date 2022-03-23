from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "ism", "famila", "yosh", "agent"
        )

class LeadForm(forms.Form):
    ism = forms.CharField(max_length=15)
    famila = forms.CharField(max_length=15)
    yosh = forms.IntegerField(min_value=8)

