# Generated by Django 4.2.16 on 2024-11-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_examenmedico'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='medicamentos/', verbose_name='Foto del Medicamento'),
        ),
    ]
