# Generated by Django 3.0.8 on 2020-07-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maps',
            name='street',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
