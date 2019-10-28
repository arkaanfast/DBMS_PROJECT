# Generated by Django 2.2.6 on 2019-10-27 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookticket', '0007_passenger_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetails',
            name='from_airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_airport_id', to='bookticket.Airport'),
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='to_airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_airport_id', to='bookticket.Airport'),
        ),
    ]
