# Generated by Django 3.2 on 2022-01-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycleapp', '0002_remove_physicalchannel_sn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalchannel',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
