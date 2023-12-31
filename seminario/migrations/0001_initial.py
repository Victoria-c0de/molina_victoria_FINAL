# Generated by Django 4.2.5 on 2023-12-21 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fecha_inscripcion', models.DateField()),
                ('hora_inscripcion', models.TimeField()),
                ('estado', models.CharField(max_length=20)),
                ('observacion', models.TextField()),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminario.institucion')),
            ],
        ),
    ]
