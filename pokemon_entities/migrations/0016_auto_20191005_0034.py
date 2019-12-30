# Generated by Django 2.2.3 on 2019-10-04 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20191004_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='previous_evolution',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolution', to='pokemon_entities.Pokemon'),
        ),
    ]