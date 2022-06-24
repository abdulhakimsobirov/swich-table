from django.contrib import admin
from .forms import SwitchForm
from .models import Switch


class SwitchAdmin(admin.ModelAdmin):
    editable_list = ['layer' ]
    list_display = ('vendor', 'id', 'model',  'layer', 'downlink', 'copper_fiber', 'poe', 'uplink_model', 'uplink', 'copper_fiber2', 'switching_cap', 'forwarding_rate', 'stack', 'power_supply', 'advanced_cup', 'network_eg', 'l3_function' )
    
    list_filter = ('vendor', 'model', 'layer', 'downlink', 'copper_fiber', 'poe', 'uplink_model', 'uplink', 'copper_fiber2', 'switching_cap', 'forwarding_rate', 'stack', 'power_supply', 'advanced_cup', 'network_eg', 'l3_function' )
    search_fields = ('vendor', 'model', 'layer', 'downlink', 'copper_fiber', 'poe', 'uplink_model', 'uplink', 'copper_fiber2', 'switching_cap', 'forwarding_rate', 'stack', 'power_supply', 'advanced_cup', 'network_eg', 'l3_function' )
    

admin.site.register(Switch, SwitchAdmin)
admin.site.site_header = "Schedule of switches"
# layer
# downlink
# copper_fiber
# poeip
# uplink
# uplink
# switching_cap
# forwarding_rate
# stack
# power_supply
# advanced_cup
# network_eg
# l3_function