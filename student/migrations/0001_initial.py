# Generated by Django 3.2.12 on 2022-03-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.TextField()),
                ('name', models.TextField(max_length=40)),
                ('stud_class', models.TextField()),
                ('department', models.TextField()),
            ],
        ),
    ]
