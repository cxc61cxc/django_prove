# Generated by Django 3.2.5 on 2021-08-01 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archivi', '0019_alter_allegato_pratica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allegato',
            name='pratica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archivi.pratica'),
        ),
    ]