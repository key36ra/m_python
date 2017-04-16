#!/usr/bin/env python
# coding: utf-8

"""
好きな軽量言語をradioフォームで入力。
投票毎に各投票数をpickleモジュールで記憶して
UIにそれぞれの総計を表示させるプログラム。
"""

import pickle
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()

# html本文内のform部分のUIオブジェクトを生成
form_body=u"""
  <form method="GET" action="/cgi-bin/picklepole.py">
    好きな軽量言語は?<br />
    %s
    <input type="submit" />
  </form>"""

# 軽量言語の選択肢を表示
# また、radioタイプの入力用UIオブジェクトを生成
radio_parts=u"""
<input type="radio" name="language" value="%s" />%s
<div style="border-left: solid %sem red; ">%s</div>
"""

lang_dic={}
# 同ディレクトリ内のfavorite_langage.datファイルを、
# ファイルオブジェクトfとして開く。ここでは読込のみ。
try:
    f=open('./favorite_langage.dat')
    lang_dic=pickle.load(f)
except IOError:
    pass

content=""
# httphandlerモジュールファイルからインポートしたRequest()クラス
# からreqインスタンスを作成
req=Request()
# クエリでlanguageに値があればそれをlangオブジェクトにいれ、
# その投票数にカウント+1する。
if req.form.has_key('language'):
    lang=req.form['language'].value
    lang_dic[lang]=lang_dic.get(lang, 0)+1

# 書き込み可能状態で、ファイルオブジェクトfを作成。
f=open('./favorite_langage.dat', 'w')
# 各軽量言語とその投票数を入れたlang_dicディクショナリを
# シリアライズして、ファイルオブジェクトfに保存。
pickle.dump(lang_dic, f)

# langを各軽量言語に対して、その言語名と投票数を入れて
# フォームオブジェクトを完成させる。
for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
    num=lang_dic.get(lang, 0)
    content+=radio_parts%(lang, lang, num, num)

res=Response()
body=form_body%content
res.set_body(get_htmltemplate()%body)
print res
