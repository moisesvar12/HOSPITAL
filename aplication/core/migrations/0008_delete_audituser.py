# Generated by Django 4.2.16 on 2024-11-15 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_tipocategoria_categoria_examen_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuditUser',
        ),
    ]
