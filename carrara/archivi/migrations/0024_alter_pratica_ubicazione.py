# Generated by Django 3.2.5 on 2021-08-09 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivi', '0023_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pratica',
            name='ubicazione',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
