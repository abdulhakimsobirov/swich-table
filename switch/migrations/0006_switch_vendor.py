# Generated by Django 4.0.5 on 2022-06-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0005_alter_switch_advanced_cup_alter_switch_copper_fiber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='vendor',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Vendor'),
        ),
    ]
