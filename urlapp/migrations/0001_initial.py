# Generated by Django 4.1.7 on 2023-03-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orginal_url', models.URLField(blank=True, max_length=700, null=True)),
                ('short_url', models.CharField(blank=True, max_length=255, null=True)),
                ('time_date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
