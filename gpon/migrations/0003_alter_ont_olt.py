# Generated by Django 3.2.9 on 2021-11-22 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpon', '0002_auto_20211121_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ont',
            name='olt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='onts', to='gpon.olt'),
        ),
    ]
