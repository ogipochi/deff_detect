from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid as uuid_lib
from datetime import datetime
import hashlib
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Setting(models.Model):
    uuid = models.UUIDField(db_index=True,default=uuid_lib.uuid4,editable=True)
    name = models.CharField('設定名',max_length=31,blank=False,null=False,unique=True)
    similarity = models.FloatField(
        '類似度',
        default=1.0,
        validators=[MinValueValidator(0.0),MaxValueValidator(1.0)])
    description = models.TextField('説明',blank=True,null=True)
    hero = models.CharField('主人公',max_length=63,default="ヒロイン")
    sheet_name = models.CharField('読み込みシート名',max_length=31,default="Story")
    start_row = models.IntegerField(default=3)
    dialog_sheet_col = models.CharField('',max_length=2,default="H")
    name_sheet_col = models.CharField('',max_length=2,default="B")
    
    def __str__(self):
        return self.name
    def conversion_table(self):
        chara_name_list = CharaName.objects.filter(setting=self.id)
        table = {}
        for chara_name in chara_name_list:
            table[chara_name.name_origin] = chara_name.name_rear
        return table

class CharaName(models.Model):
    """
    キャラクターの名前変換用のクラス
    """
    uuid = models.UUIDField(db_index=True,default=uuid_lib.uuid4,editable=False)
    setting = models.ForeignKey(Setting,on_delete=models.CASCADE)
    name_origin = models.CharField('名前（変換前）',max_length=31,unique=True)
    name_rear = models.CharField('名前(変換後)',max_length=31)
    def __str__(self):
        return self.name_origin + '==>' + self.name_rear
    class Meta:
        ordering = ['name_rear']
        unique_together = [('setting','name_origin')]


class CharaProf(models.Model):
    """
    キャラクターのプロフィールを管理するクラス
    これがある方が名前を管理しやすいと思った
    """
    setting = models.ForeignKey(Setting,on_delete=models.CASCADE)
    last_name_kanji = models.CharField('姓(漢字)',max_length=31,default="")
    first_name_kanji = models.CharField('名(漢字)',max_length=31,default="")
    last_name_kana = models.CharField('姓(かな)',max_length=31,default="")
    first_name_kana = models.CharField('名(かな)',max_length=31,default="")
    last_name_alphabet = models.CharField('姓(Alphabet)',max_length=31,default="")
    first_name_alphabet = models.CharField('名(Alphabet)',max_length=31,default="")
    name_rear = models.CharField('名前(変換後)',max_length=31)