# Generated by Django 3.0.7 on 2022-02-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_question_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
