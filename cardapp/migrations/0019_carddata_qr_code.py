# Generated by Django 4.1.5 on 2023-01-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0018_remove_carddata_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='carddata',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes/'),
        ),
    ]