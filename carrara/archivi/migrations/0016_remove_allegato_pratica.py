# Generated by Django 3.2.5 on 2021-07-31 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archivi', '0015_allegato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allegato',
            name='pratica',
        ),
    ]
