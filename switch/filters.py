

from secrets import choice
import django_filters
from django_filters import FilterSet,DateFilter,CharFilter,DateFromToRangeFilter
from django_filters.widgets import RangeWidget,CSVWidget,DateRangeWidget
from django import forms

from .models import Switch

class SwitchFilter(django_filters.FilterSet):
    choice = (
        ('24', '24'),
        ('12', '12'),
        ('48', '48'),
    )


    class Meta:
        model = Switch
        fields = ['vendor', 'layer', 'downlink', 'poe',  'power_supply', 'l3_function']

