# Generated by Django 3.2 on 2022-10-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.IntegerField(null=True),
        ),
    ]
