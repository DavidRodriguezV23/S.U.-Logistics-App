# Generated by Django 3.2.7 on 2021-09-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('n_nombres', models.EmailField(max_length=40)),
                ('n_apellido1', models.CharField(max_length=20)),
                ('n_apellido2', models.CharField(max_length=20)),
                ('k_cedula', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('f_nacimiento', models.DateField()),
                ('i_genero', models.CharField(max_length=1)),
                ('f_ingreso', models.DateField()),
                ('o_numero', models.IntegerField(default=0)),
                ('o_cargo', models.CharField(max_length=50)),
                ('o_jefe', models.IntegerField(verbose_name=-1)),
                ('o_zona', models.CharField(max_length=30)),
                ('n_municipio', models.CharField(max_length=30)),
                ('n_departamento', models.CharField(max_length=30)),
                ('v_ventas2019', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('o_email', models.EmailField(max_length=40, unique=True)),
                ('o_imagen', models.CharField(max_length=20)),
                ('o_telefono', models.DecimalField(decimal_places=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Empleado',
            },
        ),
    ]
