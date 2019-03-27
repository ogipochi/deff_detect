import unittest
import generics
from models import CharaNameList
from generics import TextToList
import sample_obj
from test_base import BaseTest


class GenericTest(BaseTest):
    def test_sample(self):
        chara_name_list = CharaNameList(self.settings[0][0])
        chara_name_list.serialize()
        for text_obj in sample_obj.sample_text:
            text_to_list = TextToList(
                text = text_obj["text"],
                version = text_obj["version"],
                conversion_table = chara_name_list.conversion_table(),
                heroin = self.settings[0][5],
                similarity = self.settings[0][3]
            )
            result = text_to_list.convert()
            print(result)
            print()
            self.assertEqual(result,text_obj["output"])


            

if __name__=='__main__':
    unittest.main()

