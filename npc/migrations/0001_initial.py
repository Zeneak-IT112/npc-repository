# Generated by Django 3.1.7 on 2021-03-19 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('type_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'persontypes',
                'db_table': 'persontype',
            },
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('type_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'placetypes',
                'db_table': 'placetype',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('place_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='npc.placetype')),
            ],
            options={
                'verbose_name_plural': 'places',
                'db_table': 'place',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('person_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='npc.persontype')),
            ],
            options={
                'verbose_name_plural': 'people',
                'db_table': 'person',
            },
        ),
    ]
