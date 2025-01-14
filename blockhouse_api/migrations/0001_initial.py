# Generated by Django 5.1.1 on 2024-09-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CandleStick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DateField()),
                ('open', models.IntegerField()),
                ('high', models.IntegerField()),
                ('low', models.IntegerField()),
                ('close', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LineChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PieChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
