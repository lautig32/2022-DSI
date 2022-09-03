# Generated by Django 4.0.5 on 2022-07-06 18:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('street', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_phone', models.CharField(blank=True, default='', max_length=20, verbose_name='Telefono')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('number_street', models.IntegerField(null=True, verbose_name='numero domicilio')),
                ('date_register_claim', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='Fecha de inicio')),
                ('date_modified_claim', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('state_local', models.CharField(choices=[('RC', 'Recibido'), ('AS', 'Asignado'), ('EE', 'En ejecución'), ('CP', 'Completado'), ('IP', 'En plan'), ('DE', 'Error de datos')], default='AS', max_length=15, verbose_name='Estado')),
                ('reception', models.CharField(choices=[('WHAT', 'whatsApp'), ('WEB', 'web')], default='WEB', max_length=15, verbose_name='recepción')),
                ('citizen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='NoteClaim_citizen', to=settings.AUTH_USER_MODEL, verbose_name='ciudadano')),
            ],
            options={
                'verbose_name': 'reclamo',
                'verbose_name_plural': 'reclamos',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='imagen representativa')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'verbose_name': 'tipo',
                'verbose_name_plural': 'tipos',
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reason_type', to='claim.type', verbose_name='tipo')),
            ],
            options={
                'verbose_name': 'motivo',
                'verbose_name_plural': 'motivos',
            },
        ),
        migrations.CreateModel(
            name='NoteClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='fecha')),
                ('note', models.TextField(verbose_name='nota')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='NoteClaim_author', to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claim.claimregister')),
            ],
            options={
                'verbose_name': 'nota',
                'verbose_name_plural': 'notas',
            },
        ),
        migrations.CreateModel(
            name='ImageClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True, verbose_name='nota')),
                ('image', models.ImageField(upload_to='', verbose_name='imagen')),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claim.claimregister')),
            ],
            options={
                'verbose_name': 'imagen',
                'verbose_name_plural': 'imágenes',
            },
        ),
        migrations.AddField(
            model_name='claimregister',
            name='reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ClaimRegister_reason', to='claim.reason', verbose_name='motivo'),
        ),
        migrations.AddField(
            model_name='claimregister',
            name='street_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ClaimRegister_street_location', to='street.street', verbose_name='domicilio'),
        ),
        migrations.AddField(
            model_name='claimregister',
            name='street_location_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ClaimRegister_street_location_a', to='street.street', verbose_name='entre calle uno'),
        ),
        migrations.AddField(
            model_name='claimregister',
            name='street_location_b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ClaimRegister_street_location_b', to='street.street', verbose_name='entre calle dos'),
        ),
        migrations.AddField(
            model_name='claimregister',
            name='user_last_change',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_last_change', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registro la ultima modificacion'),
        ),
    ]