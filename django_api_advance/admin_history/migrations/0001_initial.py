# Generated by Django 5.0.1 on 2024-02-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('login', 'Login'), ('logout', 'Logout'), ('other', 'Other')], max_length=10)),
                ('email', models.CharField(max_length=255)),
                ('user_id', models.PositiveIntegerField()),
                ('login_time', models.DateTimeField()),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('role', models.CharField(max_length=50)),
                ('session_id', models.CharField(max_length=100)),
                ('jwt_token', models.CharField(default='', max_length=255)),
            ],
        ),
    ]