# Generated by Django 3.1.2 on 2020-10-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20201011_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='upload_date',
            field=models.DateField(),
        ),
    ]
