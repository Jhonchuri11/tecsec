# Generated by Django 3.2 on 2023-12-08 05:59

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiTec', '0004_auto_20231204_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('latitud', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitud', models.DecimalField(decimal_places=8, max_digits=11)),
                ('nivel_seguridad', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Clientes',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.CreateModel(
            name='Incidentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitud', models.DecimalField(decimal_places=8, max_digits=11)),
                ('descripcion', models.TextField()),
                ('fechaCcreacion', models.DateTimeField(auto_now_add=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('id_calle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiTec.calle')),
            ],
        ),
        migrations.CreateModel(
            name='CallePeligrosas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_peligro', models.IntegerField()),
                ('idcalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiTec.calle')),
            ],
        ),
    ]
