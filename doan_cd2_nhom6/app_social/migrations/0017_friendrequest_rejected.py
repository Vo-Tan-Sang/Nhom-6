# Generated by Django 4.2.5 on 2023-10-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0016_friendrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
