# Generated by Django 2.2.6 on 2019-10-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookticket', '0006_auto_20191027_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='password',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]