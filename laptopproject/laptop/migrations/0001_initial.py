# Generated by Django 5.0.3 on 2024-03-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var_name', models.CharField(max_length=20)),
                ('year_of_manufact', models.IntegerField()),
                ('price', models.IntegerField()),
                ('outlet', models.CharField(max_length=20)),
            ],
        ),
    ]