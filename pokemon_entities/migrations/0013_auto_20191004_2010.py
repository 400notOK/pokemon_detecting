# Generated by Django 2.2.3 on 2019-10-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_pokemon_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]