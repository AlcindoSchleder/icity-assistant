# Generated by Django 2.2.12 on 2020-04-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0002_auto_20200410_1844'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='watsonaccess',
            name='watson_acce_fk_user_38c8d9_idx',
        ),
        migrations.RenameField(
            model_name='watsonaccess',
            old_name='api_key',
            new_name='component_key',
        ),
        migrations.RenameField(
            model_name='watsonaccess',
            old_name='url',
            new_name='component_url',
        ),
        migrations.RemoveField(
            model_name='watsonaccess',
            name='component_id',
        ),
        migrations.RemoveField(
            model_name='watsonaccess',
            name='fk_user',
        ),
        migrations.AddIndex(
            model_name='watsonaccess',
            index=models.Index(fields=['fk_assistants', 'fk_watson_components'], name='watson_acce_fk_assi_c0cc9a_idx'),
        ),
    ]
