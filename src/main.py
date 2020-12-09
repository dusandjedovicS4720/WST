from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
import pymysql
import re
from bson import ObjectId
from datetime import datetime
import hashlib
import time

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

# Raspored ==========================================================
@app.route('/raspored')
def raspored():
	host='localhost'
	user = 'root'
	password = ''
	db = 'raspored'
	try:
		con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8mb4')
		print('+=========================+')
		print('|  CONNECTED TO DATABASE  |')
		print('+=========================+')
	except Exception as e:
		sys.exit('error',e)
	cur = con.cursor()
	cur.execute("SELECT * FROM raspored")
	data = cur.fetchall()
	
	nastavnici = []
	ucionice = []

	for row in data:
		id = row[0]
		predmet = row[1]
		tip = row[2]
		nastavnik = row[3]
		grupe = row[4]
		dan = row[5]
		termin = row[6]
		ucionica = row[7]

		nastavnici.append(nastavnik)
		ucionice.append(ucionica)

	print('+=========================+')
	print('|  UNIQUE VALUES  |')
	print('+=========================+')

	freeUcionice = {x.replace('\n', '') for x in ucionice}
	freeNastavnici = {x.replace('\n', '') for x in nastavnici}

	uniqueUcionice = set(freeUcionice)
	uniqueNastavnici = set(freeNastavnici)
	
	print(uniqueUcionice)
	print(uniqueNastavnici)

	return render_template('raspored.html', data=data, uniqueNastavnici=uniqueNastavnici, uniqueUcionice=uniqueUcionice)
# Raspored ==========================================================


if __name__ == '__main__':
	app.run(debug=True)