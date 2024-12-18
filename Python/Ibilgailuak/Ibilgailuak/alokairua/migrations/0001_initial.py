# Generated by Django 5.1.1 on 2024-10-13 21:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kotxe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('modeloa', models.CharField(max_length=100)),
                ('matrikula', models.CharField(max_length=10, unique=True)),
                ('egoera', models.CharField(choices=[('libre', 'Libre'), ('alokatutako', 'Alokatutako')], default='libre', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pertsona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=100)),
                ('abizena', models.CharField(max_length=100)),
                ('emaila', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Alokatzea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasiera_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('amaiera_data', models.DateTimeField()),
                ('kotxea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alokairua.kotxe')),
                ('pertsona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alokairua.pertsona')),
            ],
        ),
    ]
