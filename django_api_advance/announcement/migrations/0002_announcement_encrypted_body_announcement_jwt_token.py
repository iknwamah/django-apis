# Generated by Django 5.0.1 on 2024-02-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='encrypted_body',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='announcement',
            name='jwt_token',
            field=models.CharField(default='', max_length=500),
        ),
    ]
