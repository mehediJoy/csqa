# Generated by Django 3.0.7 on 2022-02-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_answer_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
