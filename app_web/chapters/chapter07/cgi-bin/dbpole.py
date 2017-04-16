#!/usr/bin/env python
# coding: utf-8

# sqlite3, httphandler, cgitbモジュールをインポート
import sqlite3
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()

# 好きな軽量言語を入力させるフォーム形式オブジェクトformを作成
form_body=u"""
  <form method="GET" action="/cgi-bin/dbpole.py">
    好きな軽量言語は?<br />
    %s
    <input type="submit" />
  </form>"""

# radio型の入力フォームオブジェクトを形成
radio_parts=u"""
<input type="radio" name="language" value="%s" />%s
<div style="border-left: solid %sem red; ">%s</div>
"""

# カーソルと軽量言語名を引数に、更新処理を行う関数
def incrementvalue(cur, lang_name):
    # language_poleテーブルからnameがlang_name変数
    # に等しいvalueを選択
    cur.execute("""SELECT value FROM language_pole
                   WHERE name='%s'""" % lang_name)
    item=None
    # 選択したデータすべてに対して
    for item in cur.fetchall():
        cur.execute("""UPDATE language_pole
           SET value=%d WHERE name='%s'""" % (item[0]+1, lang_name))
    # SELECT文の戻り値が無かった場合
    if not item:
        cur.execute("""INSERT INTO language_pole(name, value)
                       VALUES('%s', 1)""" % lang_name)

# sqlite3のconnectメソッドからdbfile.datファイルをDBとして
# コネクションオブジェクトconを作成
con=sqlite3.connect('./dbfile.dat')
# コネクションオブジェクトconからカーソルcurを作成
cur=con.cursor()
try:
    cur.execute("""CREATE TABLE language_pole (
                   name text, value int);""")
except:
    pass

content=""
# リクエストオブジェクトの作成
req=Request()
# formにlanguage変数入力があった場合、更新処理を行う
if req.form.has_key('language'):
    incrementvalue(cur, req.form['language'].value)

lang_dic={}
cur.execute("""SELECT name, value FROM language_pole;""")
for res in cur.fetchall():
    lang_dic[res[0]]=res[1]

for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
    num=lang_dic.get(lang, 0)
    content+=radio_parts%(lang, lang, num, num)

con.commit()

res=Response()
body=form_body%content
res.set_body(get_htmltemplate()%body)
print res
