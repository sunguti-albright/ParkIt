# Generated by Django 4.0.5 on 2022-06-22 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='parking_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='parkapp.parkslot'),
        ),
    ]