#!/usr/bin/env python
# coding: utf-8

"""
クエリによるlanguageへの複数の入力に対し、それらを順番にhtml文書形式で出力
"""

# cgiモジュールをインポート
import cgi
# クエリ操作一般を担うformオブジェクトを作成
form=cgi.FieldStorage()

# 空のhtml文書オブジェクトhtml_bodyを作成
html_body = u"""
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
  </head>
  <body>
  %s
  </body>
</html>"""

# html_body本文を決めるcontentオブジェクトを定義
content=''
# クエリによってlanguageに代入された値を、enumerate形式(==(要素番号,シーケンスの要素))でcontentに代入
for cnt, item in enumerate(form.getvalue('language')):
    content+="%d : %s <br />" % (cnt+1, item)

print "Content-type: text/html\n"
print html_body % content
