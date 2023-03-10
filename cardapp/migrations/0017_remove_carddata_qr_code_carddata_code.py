# Generated by Django 4.1.5 on 2023-01-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0016_carddata_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carddata',
            name='qr_code',
        ),
        migrations.AddField(
            model_name='carddata',
            name='code',
            field=models.ImageField(blank=True, null=True, upload_to='code'),
        ),
    ]