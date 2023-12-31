# Generated by Django 3.2 on 2023-12-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTec', '0002_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('numero', models.CharField(max_length=9)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
