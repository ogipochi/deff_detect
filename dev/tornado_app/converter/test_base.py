import unittest
import generics
import pymysql.cursors


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.conn = pymysql.connect(
            host="db",
            user = "coly_rd_2018",
            password="D9o68hr9_2018",
            charset="utf8",
            db = "homepage"
        )
        with self.conn.cursor() as cur:
            sql = "SELECT id,uuid,name,similarity,description,hero FROM `character_setting`"
            cur.execute(sql)
            self.settings = cur.fetchall()