# Generated by Django 2.1.7 on 2019-03-15 04:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharaName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name_origin', models.CharField(max_length=31, unique=True, verbose_name='名前（変換前）')),
                ('name_rear', models.CharField(max_length=31, verbose_name='名前(変換後)')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.Setting')),
            ],
            options={
                'ordering': ['name_rear'],
            },
        ),
        migrations.CreateModel(
            name='CharaProf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name_kanji', models.CharField(default='', max_length=31, verbose_name='姓(漢字)')),
                ('first_name_kanji', models.CharField(default='', max_length=31, verbose_name='名(漢字)')),
                ('last_name_kana', models.CharField(default='', max_length=31, verbose_name='姓(かな)')),
                ('first_name_kana', models.CharField(default='', max_length=31, verbose_name='名(かな)')),
                ('last_name_alphabet', models.CharField(default='', max_length=31, verbose_name='姓(Alphabet)')),
                ('first_name_alphabet', models.CharField(default='', max_length=31, verbose_name='名(Alphabet)')),
                ('name_rear', models.CharField(max_length=31, verbose_name='名前(変換後)')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.Setting')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='charaname',
            unique_together={('setting', 'name_origin')},
        ),
    ]
