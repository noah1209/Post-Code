import ui
import clipboard
from console import hud_alert
import geocoder
import time
import pyperclip
text = ""
a = ""
b = ""


def button_tapped(sender):
	sender.title = 'Searching'
	v.close()
	c = a + "," + b
	print(c)


def copy(sender):
	text = sender.superview['textfield1'].text
	str1 = "{}".format(text)
	print(str1)
	ret = geocoder.osm(str1, timeout=5.0)
	global a
	global b
	a = str(ret.latlng[0])
	b = str(ret.latlng[1])


v = ui.load_view('ai.pyui')
v['imageview1'].image = ui.Image('earth.JPG')
v.present('sheet')

