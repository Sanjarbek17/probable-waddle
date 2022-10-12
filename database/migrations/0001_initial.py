# Generated by Django 4.1.2 on 2022-10-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('img_url', models.URLField(max_length=50)),
            ],
        ),
    ]