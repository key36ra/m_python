#!/usr/bin/env python
# coding: utf-8

"""
クライアントクエリによりfooに代入された値をそのままhtml文書形式で出力するプログラム
"""

# html_bodyに空のhtml文書形式を代入
html_body = u"""
<html>
  <body>
  %s
  </body>
</html>"""

# cgiモジュールをインポート
import cgi
# クエリ操作一般を担うformオブジェクトを作成
form=cgi.FieldStorage()

# クライアントからのクエリにより、fooに代入された値をhtml文書に入れて出力
print "Content-type: text/html\n"
print html_body % form['foo'].value
