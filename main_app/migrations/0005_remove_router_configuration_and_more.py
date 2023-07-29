# Generated by Django 4.2.2 on 2023-07-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_documetation_documentation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='router',
            name='configuration',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='configuration',
        ),
        migrations.AlterField(
            model_name='documentation',
            name='information',
            field=models.TextField(verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='scheduling',
            field=models.TextField(max_length=100, verbose_name='Scheduling'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='vendorContact',
            field=models.TextField(verbose_name='VendorContact'),
        ),
        migrations.AlterField(
            model_name='router',
            name='information',
            field=models.TextField(blank=True, default='', verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='information',
            field=models.TextField(blank=True, default='', verbose_name='Information'),
        ),
    ]
