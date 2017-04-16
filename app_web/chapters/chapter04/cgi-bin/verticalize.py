#!/usr/bin/env python
# coding: utf-8

"""
クエリでbodyに入れられた文章を、1行10文字として、縦書きに変換するプログラム
(横書き-縦書き変換プログラム)
"""

# cgiモジュールをインポート
import cgi
# クエリ一般の扱いを担うformオブジェクトを作成
form=cgi.FieldStorage()

# 空のhtml文書形式オブジェクトhtml_bodyを作成
html_body = u"""
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8" />
  </head>
  <body>
  %s
  </body>
</html>"""


# 文字列を行ごとに要素として入れるリストを作成
body_line=[]
# クエリでbodyに代入された値をbodyオブジェクトに入れる
body=form.getvalue('body', '')
body=unicode(body, 'utf-8', 'ignore')
# 文字列を10文字ごとに分割して、文字列のリストを作成
for cnt in range(0, len(body), 10):
    # lineにbodyの最初の10文字を入れる
    line=body[:10]
    # 10文字に満たない場合(bodyセンテンスの末尾)は、□記号を10文字まで補填
    line+=''.join([u'□' for i in range(len(line), 10)])
    # その行を1つの要素としてbody_lineリストに追加
    body_line.append(line)
    # bodyの最初の10文字以降をbodyに再代入
    body=body[10:]

# 文字列のリストを右90度に回転して、body_line_vに代入
body_line_v=[u'　'.join(reversed(x)) for x in zip(*body_line)]

# 出力
print "Content-type: text/html\n"
print (html_body % u'<br />'.join(body_line_v)).encode('utf-8', 'ignore')

