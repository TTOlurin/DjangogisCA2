# Generated by Django 4.1.1 on 2022-12-11 18:57

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path


DATA_FILENAME = 'data.json'
def load_data(apps, schema_editor):
    Restaurant = apps.get_model('world', 'Restaurants')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Restaurant(name=name, location = location).save()
            except KeyError:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_restaurants'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]