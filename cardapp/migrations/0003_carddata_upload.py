# Generated by Django 4.1.5 on 2023-01-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0002_remove_carddata_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='carddata',
            name='upload',
            field=models.ImageField(default='uploads/icon.png', upload_to='uploads/'),
        ),
    ]
