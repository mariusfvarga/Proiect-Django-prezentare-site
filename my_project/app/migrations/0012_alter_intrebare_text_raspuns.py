# Generated by Django 5.0.1 on 2024-04-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_intrebare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intrebare',
            name='text_raspuns',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
