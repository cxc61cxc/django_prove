# Generated by Django 3.2.5 on 2021-08-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivi', '0018_allegato_pratica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allegato',
            name='pratica',
            field=models.IntegerField(),
        ),
    ]
