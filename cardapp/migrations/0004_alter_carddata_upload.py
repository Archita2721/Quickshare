# Generated by Django 4.1.5 on 2023-01-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0003_carddata_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddata',
            name='upload',
            field=models.ImageField(default='uploads/icon.png', upload_to='uploads'),
        ),
    ]