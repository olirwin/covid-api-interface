from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Region


class ChooseParamsDataForm(forms.Form) :
    choices = [(region.id, region) for region in Region.objects.all()]
    region = forms.ChoiceField(label = "Region", widget = forms.Select(
            attrs = {"class" : "form-select", "aria-label" : "Choix de la région"}),
                                choices = choices, required = True)
    start_date = forms.DateField(label = "Du", widget = AdminDateWidget(
        attrs = {"class" : "form-control", "aria-label" : "Date de début"}),
                                 required = True)
    end_date = forms.DateField(label = "Au", widget = AdminDateWidget(
        attrs = {"class" : "form-control", "aria-label" : "Date de début"}),
                               required = True)

    pass
