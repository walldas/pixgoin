from flask import Flask, render_template, url_for, request, redirect,make_response, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import os
import hashlib
import random
import uuid


import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = sac.from_json_keyfile_name("seipsheet.json",scope)

app = Flask(__name__)

def box_info(data_):
	on = format(data_)
	if on =="on":
		return "uzsiregistravo"
	return "nesiregistravo"
	

def add_to_exel(now):
	try:
		client = gspread.authorize(creds)
		sheets = client.open("zymejimai").worksheets()
		sheet = sheets[0]
		col = sheet.col_values(2)
		print(len(col),col[-1])
		sheet.update_cell(len(col)+1,2,now)
	except:pass

def update_last_cell(comment,box):
	try:
		client = gspread.authorize(creds)
		sheets = client.open("zymejimai").worksheets()
		sheet = sheets[0]
		col = sheet.col_values(2)
		if len(col[-1]) == 14:
			data = col[-1] +" ("+ box +") "+ comment
			sheet.update_cell(len(col),2,data)
	except:pass
	
def data_now_():
	try:
		client = gspread.authorize(creds)
		sheets = client.open("zymejimai").worksheets()
		sheet = sheets[0]
		col = sheet.col_values(2)
		return col[::-1][:10]
	except:
		return []

	
@app.route("/")
def index():
	col = data_now_()
	return render_template("index.html",col=col)
	

@app.route("/start/",  methods=["POST","GET"])
def started():
	
	if request.method == 'POST':
		comment = request.form.get("comment")
		box = box_info(request.form.get("box"))
		update_last_cell(comment,box)
		return make_response(redirect(url_for('index')))
		
	else:
		now = format(datetime.now().strftime("%m-%d %H:%M:%S"))
		add_to_exel(now)
		return render_template("started.html")
		

	
if __name__=="__main__":
	app.run(debug=True, host="0.0.0.0", port=5000 , threaded=True)
	#80 http
	#https 443
