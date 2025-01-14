# Generated by Django 2.2.6 on 2019-10-27 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookticket', '0010_auto_20191027_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetails',
            name='from_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_airport_id', to='bookticket.Airport'),
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='to_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_airport_id', to='bookticket.Airport'),
        ),
    ]
