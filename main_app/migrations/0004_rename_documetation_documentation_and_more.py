# Generated by Django 4.2.2 on 2023-07-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_switch_configuration_alter_switch_information_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Documetation',
            new_name='Documentation',
        ),
        migrations.AlterField(
            model_name='router',
            name='configuration',
            field=models.TextField(blank=True, default='', verbose_name='Configuration'),
        ),
    ]