from django import forms
from traitlets import dlink
from .models import Switch, advanced_cup_choices



class SwitchForm(forms.ModelForm):
    # myfield = forms.MultipleChoiceField(choices=advanced_cup_choices, widget=forms.SelectMultiple)

    class Meta:
        model = Switch
        fields = "__all__"
