# Generated by Django 4.1 on 2022-08-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_alter_configuration_history_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
