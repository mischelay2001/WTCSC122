# Generated by Django 2.0.2 on 2018-04-06 08:25

from django.db import migrations
import csv

class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0003_add_golfer_city'),
    ]
    def add_city_data(apps, schema_editor):
        raw_file = open('golfersInput.csv')
        raw_file_read = csv.reader(raw_file)
        golfers = list(raw_file_read)
        for row in golfers:
            # for current row, capture and strip golfer name
            row[0] = row[0].strip()
            # for current row, capture and strip golfer birthdate
            row[1] = row[1].strip()
            # for current row, capture and strip golfer city
            row[2] = row[2].strip()
            # # append elements into golfer_list
            # golfers.append(row[0] + "," + row[1] + "," + row[2])
        Golfer = apps.get_model ('golfer', 'Golfer')
        for name, bdate, city in golfers:
            golfer = Golfer.objects.get(golfer_name=name)
            golfer.golfer_city=city
            golfer.save()

    def remove_city_data (apps, schema_editor):
        Golfer = apps.get_model ('golfer', 'Golfer')
        Golfer.objects.update (golfer_city='unknown')
    operations = [
        migrations.RunPython(add_city_data, reverse_code=remove_city_data)
    ]
