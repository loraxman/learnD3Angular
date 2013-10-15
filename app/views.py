
from app import app
import json
import random

@app.route('/')
@app.route('/index')
def index():
	return "hwlo!"

@app.route("/some_json")
def some_json():
	
	colors = ["blue","white","green","yellow","red", "brown", "black","purple"];
	arr = []
	for i in range(0, 10):
		n = random.randint(0, len(colors)-1)
		r = random.randint(0, 50)
	
		d = {"color":colors[n], "r" : r}
		arr.append(d)

	return json.dumps(arr)
		
		



