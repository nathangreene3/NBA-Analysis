import os
import sys
import sqlite3
from sqlite3 import Error

if os.path.isfile("FiveStats2017.csv"):
	file = open("FiveStats2017.csv")
	raw = file.readlines()
	file.close()
	try:
		db = sqlite3.connect("NBA.sqlite")
		cursor = db.cursor()
		for i in range(len(raw)):
			player = raw[i].split(",")	# [name, points, assists, steals, blocks, rebounds]
			#cursor.execute("INSERT INTO Players (id,name) VALUES (?,?)",(i,player[0]))
			#cursor.execute("INSERT INTO FiveStats (id,player_id,season,points,assists,steals,blocks,rebounds) VALUES (?,?,?,?,?,?,?,?)",(i,i,2017,player[1],player[2],player[3],player[4],player[5]))
			db.commit()
		db.close()
	except Error as e:
		print(e)