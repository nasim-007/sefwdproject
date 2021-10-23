# Generated by Django 3.0.10 on 2021-10-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='experts/')),
                ('social_facebook', models.URLField(blank=True, max_length=100)),
                ('social_github', models.URLField(blank=True, max_length=100)),
            ],
        ),
    ]
