# Generated by Django 3.2.12 on 2022-06-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('technologies', models.CharField(max_length=500)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('display_picture', models.FileField(upload_to='')),
            ],
        ),
    ]
