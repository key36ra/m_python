#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
from datetime import datetime

html_body = """
<html>
	<head>
		<meta http-equiv="content-type"
          content="text/html;charset=utf-8">
	</head>
	<body>
	%s
	</body>
</html>"""

content=""

form = cgi.FieldStorage()
year_str = form.getvalue("year", "")
month_str = form.getvalue("month", "")
date_str = form.getvalue("date", "")

content = "あなたの入力した日付は%s/%s/%sです。" % (year_str, month_str, date_str) 

print("Content-type: text/html;charset=utf-8\n")
print(html_body % content)




