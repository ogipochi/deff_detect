from time import sleep
import json
import pymysql.cursors
import uuid


class BaseModel:

    def connect(self):
        self.conn = pymysql.connect(
            host="db",
            user = "coly_rd_2018",
            password="D9o68hr9_2018",
            charset="utf8",
            db = "homepage"
        )
    def execute(self,sql):
        result = None
        with self.conn.cursor() as cur:
            cur.execute(sql)
            self.conn.commit()
    def get_data(self,sql):
        self.conn = pymysql.connect(
            host="db",
            user = "coly_rd_2018",
            password="D9o68hr9_2018",
            charset="utf8",
            db = "homepage"
        )
        result = None
        with self.conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
        return result

class SettingList(BaseModel):
    def __init__(self):
        sql = "SELECT id,uuid,name,similarity,description,hero,sheet_name,dialog_sheet_col,start_row FROM `character_setting`"
        self.setting_list = self.get_data(sql)
    def serialize(self):
        self.data = []
        for setting in self.setting_list:
            self.data.append(
                {
                    "id":setting[0],
                    "uuid":setting[1],
                    "name":setting[2],
                    "similarity":setting[3],
                    "description":setting[4],
                    "hero":setting[5],
                    "sheet_name":setting[6]
                }
            )

class CharaNameList(BaseModel):
    def __init__(self,setting_id=0):
        sql = "SELECT id,uuid,name_origin,name_rear FROM `character_charaname` WHERE setting_id={}".format(setting_id)
        self._chara_name_list = self.get_data(sql)
    def check_insert_data(self,insert_chara_names):
        chara_name_origin_list =[]
        checked_chara_names = []
        for chara_name in self._chara_name_list:
            chara_name_origin_list.append(chara_name[2])
        for insert_chara_name in insert_chara_names:
            if insert_chara_name["name_origin"] in chara_name_origin_list:
                continue
            else:
                checked_chara_names.append(insert_chara_name)
                chara_name_origin_list.append(insert_chara_name["name_origin"])
        return checked_chara_names
    def add_chara_names(self,chara_names,setting_id):
        insert_data = self.check_insert_data(chara_names)
        print(self._chara_name_list)
        print(insert_data)
        sql_tmp_insert = "INSERT INTO `character_charaname` (`id`, `uuid`, `name_origin`, `name_rear`, `setting_id`) VALUES (NULL, '{}', '{}', '{}', '{}');"
        #sql_tmp_update = "UPDATE `character_charaname` SET `uuid` = '{}' WHERE `character_charaname`.`name_origin` = `{}` AND `character_charaname`.`name_rear` = `{}`;"
        self.connect()
        for i,chara_name in enumerate(insert_data):
            
            chara_uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS,chara_name["name_rear"]))
            chara_uuid = chara_uuid.replace("-","")
            sql = sql_tmp_insert.format( chara_uuid, chara_name["name_origin"], chara_name["name_rear"], setting_id)
            self.execute(sql)
            
        return True
    def serialize(self):
        self.data = []
        for chara_name in self._chara_name_list:
            chara_name_obj = CharaName(
                name_origin=chara_name[2],
                name_rear=chara_name[3])
            chara_name_obj.serialize()
            self.data.append(chara_name_obj.data)
    def conversion_table(self):
        table = {}
        for chara_name in self.data:
            table[chara_name["name_origin"]] = chara_name["name_rear"]
        return table

class CharaName:
    def __init__(self,name_origin=None,name_rear=None):
        self.name_origin = name_origin or "名無し"
        self.name_rear = name_rear or "ナナシ"
    def serialize(self):
        self.data = {
            "name_origin":self.name_origin,
            "name_rear":self.name_rear
        }
