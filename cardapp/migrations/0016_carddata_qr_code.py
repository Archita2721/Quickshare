# Generated by Django 4.1.5 on 2023-01-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0015_remove_carddata_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='carddata',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]