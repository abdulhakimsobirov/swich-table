from tabnanny import verbose
from django.db import models

# Create your models here.

advanced_cup_choices = (
    ('BGP', 'BGP'), 
    ('EIGRP', 'EIGRP'),
    ('HSRP', 'HSRP'),
    ('IS-IS', 'IS-IS'),
    ('BSR', 'BSR'),
    ('MSDP', 'MSDP'),
    ('PIM-BIDIR', 'PIM-BIDIR'),
    ('* IP SLA', '* IP SLA'),
    ('OSPF', 'OSPF'),
)

class Switch(models.Model):
    verbose_name = 'Switch'
    verbose_name_plural = 'Switches'

    vendor = models.CharField(max_length=150, null=True, blank=True,  verbose_name="Vendor") 	
    model = models.CharField(max_length=150, null=True, blank=True,  verbose_name="Model") 
    layer = models.CharField(max_length=150, null=True, blank=True, verbose_name="Layer")                                      
    downlink = models.CharField(max_length=150, null=True, blank=True, verbose_name="Downlink") 
    copper_fiber = models.CharField(max_length=150, null=True, blank=True, verbose_name="Copper/Fiber")  
    poe = models.BooleanField( verbose_name="PoE") 
    uplink_model = models.CharField(max_length=150, null=True, blank=True, verbose_name="Uplink Model")
    uplink = models.CharField(max_length=150, null=True, blank=True, verbose_name="Uplink")
    copper_fiber2 = models.CharField(max_length=150, null=True, blank=True, verbose_name="Copper/Fiber2")
    switching_cap = models.CharField(max_length=150, null=True, blank=True, verbose_name="Switching capacity")
    forwarding_rate = models.CharField(max_length=150, null=True, blank=True, verbose_name="Forwarding rate")
    stack = models.BooleanField(max_length=150, verbose_name="Stack")  
    power_supply = models.CharField(max_length=150, null=True, blank=True,verbose_name="Power Supply")
    advanced_cup = models.CharField(max_length=150, null=True, blank=True, verbose_name="Advanced switch capabilities and scale")
    network_eg = models.CharField(max_length=150, null=True, blank=True, verbose_name="Network segmentation")
    l3_function = models.CharField(max_length=150, null=True, blank=True, verbose_name="L3 functions")

    


# Layer
# Downlink
# Copper/Fiber
# PoE
# Uplink
# Copper/Fiber
# Switching capacity
# Forwarding rate
# Stack
# Power Supply
# Advanced switch capabilities and scale
# Network segmentation
# L3 functions


# BGP, EIGRP, HSRP, IS-IS, BSR, MSDP, PIM-BIDIR,* IP SLA, OSPF