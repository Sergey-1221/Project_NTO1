# Generated by Django 4.1.3 on 2022-11-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0012_alter_tour_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour_order',
            name='people',
            field=models.IntegerField(default=1, verbose_name='Количество человек'),
        ),
    ]