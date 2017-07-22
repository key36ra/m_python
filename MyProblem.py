#!/usr/bin/env python3

"""
普段の悩みリストの管理プログラム
"""

from datetime import datetime
import pickle
import sqlite3

year  = None
month = None
day   = None
subject = None
element = [year, month, day]
con = sqlite3.connect("example.db")
cur = con.cursor()

buffer = ""

#year = input("year:")
#month = input("month:")
#day = input("day:")
#subject = str(input("subject:"))

print("Enter your SQL commands to execute in sqlite3.")
print("Enter a blank line to exit.")
 


while True:
	line = input()
	if line == "":
		break
	buffer += line
	if sqlite3.complete_statement(buffer):
		try:
			buffer = buffer.strip()
			cur.execute(buffer)
			
			if buffer.Istrip().upper().startswith("SELECT"):
				print(cur.fetchall())
		except sqlite3.Error as e:
			print("An error occurred:",e.args[0])
		buffer = ""
		
con.close()
