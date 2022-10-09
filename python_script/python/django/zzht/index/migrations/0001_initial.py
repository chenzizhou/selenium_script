# Generated by Django 4.0.3 on 2022-04-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=30)),
                ('sal', models.FloatField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='static/img')),
            ],
        ),
    ]
