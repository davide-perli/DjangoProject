# Generated by Django 4.2.11 on 2024-12-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gelaterie', '0007_remove_vizualizare_unique_vizualizare_per_utilizator_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='vizualizare',
            name='unique_vizualizare_per_utilizator',
        ),
        migrations.RemoveField(
            model_name='vizualizare',
            name='produs_nume',
        ),
        migrations.RemoveField(
            model_name='vizualizare',
            name='produs_pret',
        ),
        migrations.RemoveField(
            model_name='vizualizare',
            name='produs_tip',
        ),
        migrations.AddField(
            model_name='vizualizare',
            name='produs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gelaterie.informatii'),
        ),
        migrations.AddConstraint(
            model_name='vizualizare',
            constraint=models.UniqueConstraint(fields=('utilizator', 'produs'), name='unique_vizualizare_per_utilizator'),
        ),
    ]