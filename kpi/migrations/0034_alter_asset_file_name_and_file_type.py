# Generated by Django 2.2.7 on 2019-12-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0033_add_meta_ordering_export_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetfile',
            old_name='name',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='assetfile',
            name='file_type',
            field=models.CharField(choices=[('map_layer', 'map_layer'), ('form_media', 'form_media')], max_length=32),
        ),
    ]
