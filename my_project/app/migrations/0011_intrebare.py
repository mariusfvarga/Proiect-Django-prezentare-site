# Generated by Django 5.0.1 on 2024-04-12 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_producator_produs_producator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intrebare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_intrebare', models.CharField(max_length=200)),
                ('text_raspuns', models.CharField(max_length=200)),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produs')),
            ],
        ),
    ]
