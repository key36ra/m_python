#!/usr/bin/env python
# coding: utf-8

"""
クライアント入力の西暦に、合計いくつの金曜日があるかを、html文書として出力するプログラム(==find13f.py)
さらにcontentに加えて、西暦を選択させるoptions機能を追加
"""

# cgiモジュールをインポート
import cgi
# クエリ操作一般を担うformオブジェクトを作成
from datetime import datetime

# html本文オブジェクトを作成
# クライアントに任意の西暦の入力を求め、それをyearに代入
html_body = u"""
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8" />
  </head>
  <body>
  <form method="POST" action="/cgi-bin/find13f.py">
    西暦を選んでください:
    <select name="year">
      %s
    </select>
    <input type="submit" />
  </form>
  %s
  </body>
</html>"""

# 出力のための文章とoption属性のオブジェクトを生成
options=''
content=''

# nowに今の日時情報を入れる
now=datetime.now()
# 10年前から10年後までスキャンして、今年だけ選択
# 今年をoptionsオブジェクトにhtmlの<option select>属性の形で追加する
for y in range(now.year-10, now.year+10):
    if y!=now.year:
        select=''
    else:
        select=' selected="selected"'
    options+="<option%s>%d</option>" % (select, y)

# cgi.FieldStorage()関数のformインスタンスを作成
form=cgi.FieldStorage()
# form.getvalue()にyearと空白を代入したyear_strインスタンスを作成
year_str=form.getvalue('year', '')
# 選択した年の金曜日を走査して、該当する度にcontentに文章を入れるループ
if year_str.isdigit():
    year=int(year_str)
    friday13=0
    # 1から13月までについて、その月の13日が金曜日か確認し、該当する場合はcontentに追加
    for month in range(1, 13):
        date=datetime(year, month, 13)
        if date.weekday()==4:
            friday13+=1
            content+=u"%d年%d月13日は金曜日です" % (year, date.month)
            content+=u"<br />"

    # 入力yearに金曜日が1つでもあれば、その合計についてのまとめをcontentに追加
    if friday13:
        content+=u"%d年には合計%d個の13日の金曜日があります" % (year, friday13)
    else:
        content+=u"%d年には13日の金曜日がありません"

# 出力
print "Content-type: text/html;charset=utf-8\n"
print html_body % (options, content)
