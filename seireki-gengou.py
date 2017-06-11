#!/usr/bin/env python3

"""
We post our birthday.
And this code translate the year to the gengou,
for example "heisei", "shouwa" and so on.
"""

from datetime import datetime

now = datetime.now()

print("あなたの生まれ年(西暦)を元号に変換します")

# python3では、input()はstr型になっている(python2はint型)
year = int(input("生まれ年:"))

print()

if year in range(1868, now.year):
    print("あなたの生まれ年は、元号で表すと、")
    if year in range(1868, 1912):
        print("明治{}年".format(year-1867))
    elif year in range(1913, 1926):
        print("大正{}年".format(year-1911))
    elif year in range(1926, 1989):
        print("昭和{}年".format(year-1925))
    elif year in range(1989, now.year+1):
        print("平成{}年".format(year-1988))
    print("です。")
else:
    print("すんまへんな。明治から平成しかわかりまへんで!(_ _)!")
