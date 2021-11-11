# Generated by Django 3.2.7 on 2021-10-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nimuit', '0008_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
