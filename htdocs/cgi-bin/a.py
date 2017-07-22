print("Content-type: text/html\n")
fopen = open("cgi-bin/a.tpl", encoding="utf-8")
lines = fopen.read()
fopen.close()
print(lines)

