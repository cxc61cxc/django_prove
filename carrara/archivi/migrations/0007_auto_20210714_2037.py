# Generated by Django 3.2.4 on 2021-07-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivi', '0006_auto_20210714_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pratica',
            name='data_atto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pratica',
            name='data_prot_gen',
            field=models.DateField(null=True),
        ),
    ]
