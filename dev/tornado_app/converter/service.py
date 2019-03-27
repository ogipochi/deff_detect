from models import CharaNameList,SettingList
from http import HTTPStatus
from tornado import web , escape , ioloop , httpclient , gen
from datetime import date
import json
from generics import TextToList,DeffDetecter
import base64 , os , sys
import pandas as pd
import hashlib
import re



class Application(web.Application):
    def __init__(self,**kwargs):
        handlers = [
            (r"/api/chara_names/(\d+)/",CharaNameHandler),
            (r"/api/settings/",SettingHandler),
            (r"/api/text_to_list/",TextToListHandler),
            (r"/api/generate_deff/",GenerateDeffHandler),
        ]
        super(Application, self).__init__(handlers, **kwargs) 

class SettingHandler(web.RequestHandler):
    SUPPORTED_METHODS = ('GET')
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET')
    def get(self):
        setting_list = SettingList()
        setting_list.serialize()
        response = {
            'data':setting_list.data
        }
        self.write(response)

class CharaNameHandler(web.RequestHandler):
    SUPPORTED_METHODS = ('GET','POST')
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
    def get(self,setting_id):
        chara_name_list = CharaNameList(setting_id=setting_id)
        chara_name_list.serialize()
        response = {
            'data':chara_name_list.data
        }
        self.set_status(HTTPStatus.OK)
        self.write(response)
    def post(self,setting_id):
        data = json.loads(self.request.body)
        chara_names = []
        for name_obj in data:
            if name_obj['checked']:
                chara_names.append(
                    {
                        "name_rear":name_obj["nameRear"],
                         "name_origin":name_obj["nameOrigin"],
                    }
                )
        chara_name_list = CharaNameList(setting_id)
        result = chara_name_list.add_chara_names(chara_names,setting_id)
        response = {
            "status":10
        }
        self.set_status(HTTPStatus.OK)
        self.write(response)
class TextToListHandler(web.RequestHandler):
    SUPPORTED_METHODS = ('POST')
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST')
    def post(self):
        data = json.loads(self.request.body)
        text = data["text"]
        similarity = data["similarity"]
        heroin = data["hero"]
        version = data["version"]
        waiting_id = data["waitingId"]
        setting_id = data["settingId"]
        name_detect = data["nameDetect"]
        chara_name_list = CharaNameList(setting_id=setting_id)
        chara_name_list.serialize()
        conversion_table = chara_name_list.conversion_table()
        text_to_list = TextToList(text,version,conversion_table,heroin,similarity,int(name_detect)==1)
        result = text_to_list.convert()
        name_eval_list = text_to_list.name_eval_list
        # 重複を削除
        name_eval_list = list(set(name_eval_list))
        response = {
            "data":{
                "result":result,
                "waiting_id":int(waiting_id),
                "name_eval_list":name_eval_list
                },
        }

        self.set_status(HTTPStatus.OK)
        self.write(response)

class GenerateDeffHandler(web.RequestHandler):
    SUPPORTED_METHODS = ('POST')
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST')
    def post(self):
        data = json.loads(self.request.body)
        text_list = data["textList"]
        waiting_id = data["waitingId"]
        hero = data["hero"]
        similarity = data["similarity"]
        file_data = data["fileData"].split(";base64,")[-1].encode()
        file_type = data["fileType"]
        versioin = data["version"]
        # まずローカルにデータを保存する
        
        prefix = hashlib.sha224(self.request.body).hexdigest()
        # print("".join(file_data))
        filename = "{}.xlsx".format(prefix)
        data_dir = "./original_file"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        file_path = os.path.join(data_dir,filename)
        with open(file_path,"wb") as f:
            f.write(base64.decodebytes(file_data))
        xl_file = pd.ExcelFile(file_path)

        dfs = {}
        sheet_name_id_dict = {}
        for i,sheet_name in enumerate(xl_file.sheet_names):
            if (re.findall("[0-9]",sheet_name)):
                sheet_id = re.findall("[0-9]+",sheet_name)[0]
                dfs[sheet_name] =  xl_file.parse(sheet_name)
                sheet_name_id_dict[int(sheet_id)] = sheet_name
            elif (re.findall("[０-９]",sheet_name)):
                sheet_id = re.findall("[０-９]+",sheet_name)[0]
                dfs[sheet_name] =  xl_file.parse(sheet_name)
                sheet_name_id_dict[int(sheet_id)] = sheet_name
        deff_detecter = DeffDetecter(
            data_frames=dfs,
            data_frame_ids=sheet_name_id_dict,
            text_list = text_list,
            version = int(version)
            )
        deff_list = deff_detecter.detect()
        file_path = deff_detecter.create_wb(waiting_id)
        response = {
            "data":{
                "file_path":file_path,
                "waiting_id":waiting_id
            }
        }
        self.set_status(HTTPStatus.OK)
        self.write(response)


if __name__ == "__main__":
    application = Application()
    port = 8888
    print("Listening at port {}".format(port))
    application.listen(port)
    tornado_ioloop = ioloop.IOLoop.instance() 
    periodic_callback = ioloop.PeriodicCallback(lambda: None, 500) 
    periodic_callback.start() 
    tornado_ioloop.start()