# Generated by Django 5.0.1 on 2024-02-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reset', '0002_passwordreset_delete_resetpasswordtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordreset',
            name='hashed_password',
        ),
        migrations.AlterField(
            model_name='passwordreset',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
