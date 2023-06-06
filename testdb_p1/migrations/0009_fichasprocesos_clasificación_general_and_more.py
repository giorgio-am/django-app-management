# Generated by Django 4.0.4 on 2022-06-08 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testdb_p1', '0008_fichasprocesos_clasificación_general_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichasprocesos',
            name='macroproceso_padre',
            field=models.ForeignKey(blank=True, db_column='macroproceso_padre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='hijos', to='testdb_p1.fichasprocesos'),
        ),
    ]
