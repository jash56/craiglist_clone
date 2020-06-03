# Generated by Django 3.0.6 on 2020-06-03 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200602_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='area',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='search',
            name='created',
            field=models.DateTimeField(),
        ),
    ]