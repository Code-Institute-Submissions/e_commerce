# Generated by Django 2.0.6 on 2018-08-24 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20180824_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaselineitem',
            old_name='order',
            new_name='purchase',
        ),
    ]
