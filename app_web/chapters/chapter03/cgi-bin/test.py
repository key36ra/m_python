#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
現在の日時データ(年、月、日、時間、分、秒)をhtml文書形式にデコードして出力
"""

#日時データに関する標準ライブラリdatetimeをインポート
import datetime

#html_bodyオブジェクトに表示させたいhtml文書の本文を入れる
#html_bodyオブジェクトには後でdatetime.nowの現日時情報を入れる
html_body = """
<html><body>
%d/%d/%d %d:%d:%d
</body></html>"""

#nowオブジェクトに、datetime.datetime.now()を用いて現在の時刻を入れる
now=datetime.datetime.now()

#おまじない?
print "Content-type: text/html\n"
#html_bodyオブジェクトに現在の、now.year(年)、now.month(月)、now.day(日)、
#now.hour(時間)、now.minute(分)、now.second(秒)を代入して、表示
print html_body % (now.year, now.month, now.day, 
                   now.hour, now.minute, now.second)


