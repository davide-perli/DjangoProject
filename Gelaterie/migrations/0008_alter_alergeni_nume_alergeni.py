# Generated by Django 4.2.11 on 2024-11-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gelaterie', '0007_alter_prajituri_nume_prajitura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alergeni',
            name='nume_alergeni',
            field=models.CharField(choices=[('LACTOZA', 'lactoza'), ('GLUETEN', 'gluten'), ('ALUNE', 'alune'), ('NONE', 'none')], default='NONE'),
        ),
    ]