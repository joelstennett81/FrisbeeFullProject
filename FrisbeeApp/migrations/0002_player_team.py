# Generated by Django 2.2.25 on 2021-12-09 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrisbeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='FrisbeeApp.Team'),
        ),
    ]