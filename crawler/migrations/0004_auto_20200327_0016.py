# Generated by Django 2.2.3 on 2020-03-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_auto_20200327_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseitem_dj',
            name='atk',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='attack_distance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='buy_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='defense',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='matk',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='refinable',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='sell_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baseitem_dj',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
