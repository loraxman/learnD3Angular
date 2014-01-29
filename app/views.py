
from app import app
import json
import random
from flask import render_template
import urllib2
import models
@app.route('/')
@app.route('/index')
def index():
	return "hwlo!"

@app.route("/some_json")
def some_json():
	
	colors = ["blue","white","green","yellow","red", "brown", "black","purple", "grey","orange","#DE2669"];
	arr = []
	for i in range(0, 10):
		n = random.randint(0, len(colors)-1)
		r = random.randint(0, 50)
		d = {"color":colors[n], "r" : r}
	
		arr.append(d)

	return json.dumps(arr)



@app.route("/metadata_json")		
def metadata_json():
	items = models.getall()
	print len(items)
	arr = []
	for i in items:
		
		d = i
	
		arr.append(d)

	return json.dumps(arr)


@app.route("/metadata_json3")		
def metadata_json3():
	items = open("C:/proj/cats/tabs/res.csv").read()
	items = items.split("\n")
	
	
	arr = []
	for i in items[0:15]:
		row = i.split(",")
		
		d = {"metadata":row[2]}
	
		arr.append(d)

	return json.dumps(arr)
		
		
		
@app.route("/testtempl")
def testtempl():

	response = urllib2.urlopen('http://hub.healthdata.gov/api/2/rest/dataset')
	lnks = json.loads(response.read())
	return render_template("test.html", resp=lnks)		

@app.route("/getdetails/<data>")
def getdetails(data):
	print 'http://hub.healthdata.gov/api/2/rest/dataset/'+data
	resp = urllib2.urlopen('http://hub.healthdata.gov/api/2/rest/dataset/'+data)
	t = resp.read()
	parsed = json.loads(t)
	print parsed['url']
	return t


