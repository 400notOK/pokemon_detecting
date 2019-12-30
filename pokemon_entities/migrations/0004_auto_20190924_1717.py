# Generated by Django 2.2.3 on 2019-09-24 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_pokemonentity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon')),
            ],
        ),
        migrations.DeleteModel(
            name='PokemonEntity',
        ),
    ]