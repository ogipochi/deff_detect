# Generated by Django 2.1.7 on 2019-03-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_setting_sheet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='dialog_sheet_col',
            field=models.CharField(default='H', max_length=2, verbose_name=''),
        ),
        migrations.AddField(
            model_name='setting',
            name='name_sheet_col',
            field=models.CharField(default='B', max_length=2, verbose_name=''),
        ),
        migrations.AddField(
            model_name='setting',
            name='start_row',
            field=models.IntegerField(default=3),
        ),
    ]
