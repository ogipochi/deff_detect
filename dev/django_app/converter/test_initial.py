from character.models import *
from character.sample_obj import *

# データベースのリセット
Setting.objects.all().delete()
CharaName.objects.all().delete()

# サンプルの設定データの作成
setting_1 = Setting.objects.create(
    name="差異抽出"
)
Setting.objects.create(
    name="サンプル２"
)
Setting.objects.create(
    name="サンプル３"
)
Setting.objects.create(
    name="サンプル４"
)

# キャラクター名の作成

for chara_name in chara_name_list:
    CharaName.objects.create(
        setting = setting_1,
        name_origin=chara_name["name_origin"],
        name_rear = chara_name["name_rear"]
    )
