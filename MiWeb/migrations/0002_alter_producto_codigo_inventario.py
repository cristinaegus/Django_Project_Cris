# Generated by Django 5.2.3 on 2025-06-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_inventario',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
