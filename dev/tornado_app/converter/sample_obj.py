sample_text = [
    {
        "version":1,
        "text":"""
◯車内（昼）
;SE　飛ばす走行音

やりきれなさの全てを込めた激しい吐息と同時にハンドルに突っ伏し、私は低い唸り声を漏らす。

奥歯を噛みしめても堪えきれず、尖った感情がこぼれた。

ヒロイン
「……っ」

宮瀬豪
「一つ一つの花や木の様子を見ながら水をやる時間は、楽しいものです」
「まるで家族の食卓のようです」



;※（８話）

miyase
「毎日が、楽しいだけだったらいいのになって」
ケミカル田中
「なかなか、そういう訳にはいきませんけどね」
宮瀬豪
「だって、ちょっと辛いなって時とか、つまらないなって時がないと」
miyase
「きっと人間って、楽しかったり幸せだったりする時間を、当たり前だと思っちゃうんじゃないでしょうか」

ケミカル田中※表情差分:ニッコリ
「宮瀬さんを抱きしめて温める腕はそのままに、私は顔だけを少し離して、彼の表情を正面から見つめた。」
「いけないという訳ではないですけど……」　※表情差分:メイン

宮瀬豪※表情差分:ニッコリ
「幸せな世界で笑ってる宮瀬さんを隣で見ていたい」※表情差分:メイン

（もっと楽しくて、幸せな世界を見せてあげたい）

（今、彼の命のために伝える言の葉は、芽吹きの末に生い茂っている。）


◯宮瀬の別宅（昼）
;SE　ドアの開閉音
;SE　室内を駆け抜ける足音




◯宮瀬・秘密の庭（昼・曇り）

ガッチャマン
「そう言ってポケットからハンカチを取り出すと、それを私の首に当てた。」

海野沙知　※表情差分：悲しみ
「なに笑ってんだ？」

多田野元
「そんな罵詈雑言も、やがて消えてしまった。」
「大きな奴には大きく執れる行いを、少しも構えず、こだわらず、天真爛漫にやるのが西郷だ。」

宮瀬豪・ケミカル田中
「は、無駄だよマトリちゃん」

渡されたのは、ナチュラルなカジュアルドレスだ。

ケミカル田中・宮瀬豪　※表情差分:メイン
「このあと九条が招待されているパーティーに同行予定だったんだ」
「いえ、今日はこのまま直帰予定ですけど」
"""
    ,
    "output":[
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # ○は追加要素
            "type":"addition",
            "name":[],
            "content":"◯車内（昼）",
            "remarks":""
        },
        {
            # ;は追加要素
            "type":"addition",
            "name":[],
            "content":";SE　飛ばす走行音",
            "remarks":""
        },
           {
               # 空の改行
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # カッコがない文章はモノローグ
            "type":"mono",
            "name":[],
            "content":"やりきれなさの全てを込めた激しい吐息と同時にハンドルに突っ伏し、私は低い唸り声を漏らす。",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            "type":"mono",
            "name":[],
            "content":"奥歯を噛みしめても堪えきれず、尖った感情がこぼれた。",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # ヒロインは別で認識
            "type":"hero",
            "name":["ヒロイン",],
            "content":"「……っ」",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 改行が入りデータベースにある名前が出たあとのカッコは会話文
            "type":"dialog",
            "name":["miyase",],
            "content":"「一つ一つの花や木の様子を見ながら水をやる時間は、楽しいものです」",
            "remarks":""
        },
        {
            # 名前が入らず連続でカッコの文が来たとき会話文
            "type":"dialog",
            "name":["miyase",],
            "content":"「まるで家族の食卓のようです」",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # ;は追加要素
            "type":"addition",
            "name":[],
            "content":";※（８話）",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 名前の登録に関しては変換後の名前に統一される
            "type":"dialog",
            "name":["miyase",],
            "content":"「毎日が、楽しいだけだったらいいのになって」",
            "remarks":""
        },
        {
            # 全員の名前が認識できるかチェック
            "type":"dialog",
            "name":["tanaka",],
            "content":"「なかなか、そういう訳にはいきませんけどね」",
            "remarks":""
        },
        {
            "type":"dialog",
            "name":["miyase",],
            "content":"「だって、ちょっと辛いなって時とか、つまらないなって時がないと」",
            "remarks":""
        },
        {
            # 変換前の名前は登録してある名前に統一される
            "type":"dialog",
            "name":["miyase",],
            "content":"「きっと人間って、楽しかったり幸せだったりする時間を、当たり前だと思っちゃうんじゃないでしょうか」",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
         {
             # 名前のあとの※は一番目の文章のremarksに入る
            "type":"dialog",
            "name":["tanaka",],
            "content":"「宮瀬さんを抱きしめて温める腕はそのままに、私は顔だけを少し離して、彼の表情を正面から見つめた。」",
            "remarks":"※表情差分:ニッコリ"
        },
        {
             # 文章のあとの※はその文章のremarksに入る
            "type":"dialog",
            "name":["tanaka",],
            "content":"「いけないという訳ではないですけど……」",
            "remarks":"※表情差分:メイン"
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 名前後の※より文章後の※が優先される
            "type":"dialog",
            "name":["miyase",],
            "content":"「幸せな世界で笑ってる宮瀬さんを隣で見ていたい」",
            "remarks":"※表情差分:メイン"
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            #　（）はヒロインの会話文になる
            "type":"mono",
            "name":[],
            "content":"（もっと楽しくて、幸せな世界を見せてあげたい）",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            #　（）はヒロインの会話文になる
            "type":"mono",
            "name":[],
            "content":"（今、彼の命のために伝える言の葉は、芽吹きの末に生い茂っている。）",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 連続したaddition
            "type":"addition",
            "name":[],
            "content":"◯宮瀬の別宅（昼）",
            "remarks":""
        },
        {
            "type":"addition",
            "name":[],
            "content":";SE　ドアの開閉音",
            "remarks":""
        },
        {
            "type":"addition",
            "name":[],
            "content":";SE　室内を駆け抜ける足音",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 改行がいくつ入っても文章があれば変換される
            "type":"addition",
            "name":[],
            "content":"◯宮瀬・秘密の庭（昼・曇り）",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # データにない名前も少ない文字数＋。終わりで無いなら会話文になる
            "type":"dialog",
            "name":["ガッチャマン",],
            "content":"「そう言ってポケットからハンカチを取り出すと、それを私の首に当てた。」",
            "remarks":""
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            #データにない名前に関しても※など使用可能
            "type":"dialog",
            "name":["海野沙知",],
            "content":"「なに笑ってんだ？」",
            "remarks":"※表情差分：悲しみ"
        },
         {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {

            "type":"dialog",
            "name":["多田野元",],
            "content":"「そんな罵詈雑言も、やがて消えてしまった。」",
            "remarks":""
        },
        {
            "type":"dialog",
            "name":["多田野元",],
            "content":"「大きな奴には大きく執れる行いを、少しも構えず、こだわらず、天真爛漫にやるのが西郷だ。」",
            "remarks":""
        },
       {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 複数人の名前でも・でわけられていれば問題なく変換できる
            "type":"dialog",
            "name":["miyase","tanaka"],
            "content":"「は、無駄だよマトリちゃん」",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            "type":"mono",
            "name":[],
            "content":"渡されたのは、ナチュラルなカジュアルドレスだ。",
            "remarks":""
        },
        {
            "type":"blank",
            "name":[],
            "content":"",
            "remarks":""
        },
        {
            # 複数人の名前でも※が認識される
            "type":"dialog",
            "name":["tanaka","miyase"],
            "content":"「このあと九条が招待されているパーティーに同行予定だったんだ」",
            "remarks":"※表情差分:メイン"
        },
        {
            "type":"dialog",
            "name":["tanaka","miyase"],
            "content":"「いえ、今日はこのまま直帰予定ですけど」",
            "remarks":""
        },


    ],
    "name_eval":["ガッチャマン","海野沙知","多田野元"]
    },
    {
        "version":2,
        "text":"""

■1話【胡利衣学園・校門前（夕）】
T
やりきれなさの全てを込めた激しい吐息と同時にハンドルに突っ伏し、
私は低い唸り声を漏らす。

奥歯を噛みしめても堪えきれず、
尖った感情がこぼれた。

ヒロイン
（……１６時か。
もうそろそろかな）

ケミカル田中
お姉さん、誰か待ってるんですか？
俺、よかったら呼んできますよ

宮瀬豪
もー、いいからお前ら帰れって。
みっちゃんには言うなよ！

いやー、すみません。
おバカばっかりで

ヒロイン
ああ、いえいえ。
お気遣いを、どうもありがとう

でも多分、もうすぐ……

miyase（微妙な顔）
少なくとも、彼は
カナメくんのこと
すごく好きなんだろうなと

【街中（昼）※S1カナメマップ111b～112a回想】

カナメ
そう言って本当に
怪しくない奴
あんまり知らないんだけど



        """
    }
]