#!/usr/bin/env python
# coding: utf-8

"""
クライアント入力の西暦に、合計いくつの金曜日があるかを、html文書として出力するプログラム
"""

# cgiモジュールとdatetimeモジュールをインポート
import cgi
from datetime import datetime

# htmlの本文オブジェクトhtml_bodyを作成
# html_bodyの中身は空
html_body = u"""
<html><head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
  </head>
  <body>
  %s
  </body>
</html>"""

# html_bodyの本文に追加するcontentオブジェクトを作成
content=''

# クエリ操作一般を担うformオブジェクトを作成
form=cgi.FieldStorage()
# クエリによりyearで受け取った値を扱うyear_strオブジェクトを作成
year_str=form.getvalue('year', '')

# 最初の、入力がなくyear_strが空の状態のときに、西暦の入力を求める
if not year_str.isdigit():
    content=u"西暦を入力してください"
# 入力があった場合
else:
    # yearに入力西暦を代入し、13日金曜日のカウンターfriday13を定義
    year=int(year_str)
    friday13=0
    # 1から13月について、その13日が金曜日かどうかを走査する
    for month in range(1, 13):
        date=datetime(year, month, 13)
        # 金曜日であればfriday13にカウントさせて、文章を追加
        if date.weekday()==4:
            friday13+=1
            content+=u"%d年%d月13日は金曜日です" % (year, date.month)
            content+=u"<br />"

    # friday13が一つでもあれば、その合計をcontentに文章で、書き込む
    if friday13:
        content+=u"%d年には合計%d個の13日の金曜日があります" % (year, friday13)
    else:
        content+=u"%d年には13日の金曜日がありません"

print "Content-type: text/html;charset=utf-8\n"
print (html_body % content).encode('utf-8')
