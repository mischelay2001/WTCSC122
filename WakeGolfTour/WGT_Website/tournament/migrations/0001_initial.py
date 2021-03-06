# Generated by Django 2.0.2 on 2018-03-08 01:55

from django.db import migrations, models


# noinspection SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_id', models.IntegerField()),
                ('round_day', models.TextField()),
            ],
            options={
                'db_table': 'Round',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tourn_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tourn_name', models.TextField()),
                ('tourn_start_date', models.DateField()),
                ('tourn_num_rounds', models.IntegerField()),
                ('tourn_num_golfers', models.IntegerField()),
            ],
            options={
                'db_table': 'Tournament',
                'managed': False,
            },
        ),
    ]
