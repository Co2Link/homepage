# Generated by Django 2.2.3 on 2020-03-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_auto_20200327_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseitem_dj',
            name='item_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
