#coding:  utf-8 
import ui
import clipboard
from console import hud_alert
import geocoder
import time
import pyperclip
import requests
import json

text = ""
a = ""
b = ""


def button_tapped(sender):
	sender.title = 'Searching'
	print(a+','+b)
	v.close()
	


def copy(sender):
	text = sender.superview['textfield1'].text
	str1 = "{}".format(text)
	print('入力された文字='+str1)
	print()
	ret = geocoder.osm(str1, timeout=5.0)
	global a
	global b
	a = str(ret.latlng[0])
	b = str(ret.latlng[1])
	url = "https://geoapi.heartrails.com/api/json?method=searchByGeoLocation&x={x}&y={y}"
	url1 = url.format(x=b,y=a)
	response = requests.get(url1)
	data = response.json()
	jsontext = json.dumps(data,indent=3)
	jsontext.encode("UTF-8","replace")
	
	f = open('Where.json', 'w', encoding='UTF-8')
	f.write(jsontext)
	f.close()
	f1 = open('Where.json', 'r', encoding='UTF-8')
	jsn = json.load(f1)
	for i in range (10):
		
		c=jsn["response"]["location"][i]['city']
		d=jsn["response"]["location"][i]['town']
		f=jsn["response"]["location"][i]['postal']
		print(c)
		print(d)
		print(f)
		print()
v = ui.load_view('ai.pyui')
v['imageview1'].image = ui.Image('earth.JPG')
v.present('sheet')

