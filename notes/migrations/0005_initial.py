# Generated by Django 5.0 on 2023-12-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notes', '0004_delete_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('notes', models.TextField()),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
