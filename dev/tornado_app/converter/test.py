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
        text_to_list = TextToList(
            text = sample_obj.sample_text[0]["text"],
            version = sample_obj.sample_text[0]["version"],
            conversion_table = chara_name_list.conversion_table(),
            heroin = self.settings[0][5],
            similarity = self.settings[0][3]
        )
        result = text_to_list.convert()
        self.assertEqual(result,sample_obj.sample_text[0]["output"])


            

if __name__=='__main__':
    unittest.main()

