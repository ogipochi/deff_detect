# Generated by Django 2.1.7 on 2019-03-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_auto_20190321_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charaname',
            name='name_origin',
            field=models.CharField(max_length=31, verbose_name='名前（変換前）'),
        ),
    ]