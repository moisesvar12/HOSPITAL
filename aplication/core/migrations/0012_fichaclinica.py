# Generated by Django 4.2.16 on 2024-11-22 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_certificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_consulta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de la Consulta')),
                ('motivo_consulta', models.TextField(verbose_name='Motivo de la Consulta')),
                ('diagnostico', models.TextField(blank=True, null=True, verbose_name='Diagnóstico')),
                ('tratamiento', models.TextField(blank=True, null=True, verbose_name='Tratamiento Recomendado')),
                ('notas', models.TextField(blank=True, null=True, verbose_name='Notas Adicionales')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fichas_clinicas', to='core.doctor', verbose_name='Doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fichas_clinicas', to='core.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Ficha Clínica',
                'verbose_name_plural': 'Fichas Clínicas',
                'ordering': ['-fecha_consulta'],
            },
        ),
    ]
