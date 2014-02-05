
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



@app.route("/gsa_json")	
def gsa_json():
	data = [
		{"airline":"9G Rail Limited","count":13},
{"airline":"Adria Airways - The Airline of Slovenia","count":13},
{"airline":"Aegean Airlines S.A.","count":15},
{"airline":"Aer Arann Express (Comharbairt Gaillimh Teo)","count":13},
{"airline":"Aer Lingus Limited","count":13},
{"airline":"Aerocomercial Oriente Norte Ltda","count":13},
{"airline":"Aerolineas Argentinas S.A.","count":11},
{"airline":"Aerolineas Galapagos S.A. Aerogal","count":13},
{"airline":"Aeromexico Aerovias de Mexico S.A. de C.V.","count":12},
{"airline":"Aerosvit Airlines","count":1},
{"airline":"Aerovias del Continente Americano S.A AVIANCA","count":13},
{"airline":"Afriqiyah Airways","count":15},
{"airline":"Air Astana","count":1},
{"airline":"Air Austral","count":16},
{"airline":"Air Baltic Corporation AS","count":14},
{"airline":"Air Botswana","count":13},
{"airline":"Air Burkina","count":15},
{"airline":"Air Caledonie International","count":12},
{"airline":"Air Europa Lineas Aereas, S.A.","count":13},
{"airline":"Air India Limited","count":1},
{"airline":"Air Macau Company Limited","count":7},
{"airline":"Air Madagascar","count":8},
{"airline":"Air Malawi Limited","count":13},
{"airline":"Air Malta p.l.c.","count":13},
{"airline":"Air Mauritius","count":7},
{"airline":"Air Moldova","count":13},
{"airline":"Air Namibia","count":9},
{"airline":"Air Niamey","count":7},
{"airline":"Air One S.p.A","count":13},
{"airline":"Air Pacific Limited t/a Fiji Airways","count":3},
{"airline":"Air Seychelles Limited","count":6},
{"airline":"Air Tahiti Nui","count":13},
{"airline":"Air Tanzania Company Ltd.","count":13},
{"airline":"Air Vanuatu (Operations) Limited","count":18},
{"airline":"Air Zimbabwe (Pvt) Ltd.","count":18},
{"airline":"Aircompany Asian Express Airline LLC","count":13},
{"airline":"Aircompany KHORS Ltd.","count":5},
{"airline":"Aircompany Polet","count":13},
{"airline":"Airline Utair - Ukraine","count":18},
{"airline":"Airlines Air Onix","count":18},
{"airline":"Alaska Airlines Inc.","count":13},
{"airline":"Alaska Juneau Aeronautics Inc dba Wings of Alaska","count":15},
{"airline":"Alitalia-Compagnia Aerea Italiana S.p.A","count":1},
{"airline":"All Nippon Airways Co. Ltd.","count":1},
{"airline":"Amaszonas S.A.","count":13},
{"airline":"Arik Air Limited","count":13},
{"airline":"Arkia - Israeli Airlines Ltd","count":13},
{"airline":"Armavia","count":15},
{"airline":"Asiana Airlines Inc.","count":2},
{"airline":"Atlasjet Airlines Inc.","count":13},
{"airline":"Azerbaijan Hava Yollary","count":9},
{"airline":"B & H Airlines","count":13},
{"airline":"BV Airways dba BVI Airways","count":16},
{"airline":"Bahamasair Holdings, Limited","count":13},
{"airline":"Bangkok Airways Public Company Limited","count":4},
{"airline":"Belavia","count":16},
{"airline":"Berjaya Air Sdn. Bhd.","count":11},
{"airline":"Biman Bangladesh Airlines","count":13},
{"airline":"Binter Canarias","count":13},
{"airline":"Blue Panorama Airlines S.p.A.","count":11},
{"airline":"Braathens Regional AB","count":13},
{"airline":"Bradley Air Services Limited t/a First Air","count":16},
{"airline":"Brussels Airlines N.V.","count":7},
{"airline":"Bulgaria Air","count":13},
{"airline":"Buraq Air Transport (BRQ)","count":13},
{"airline":"CONVIASA","count":18},
{"airline":"Cambodia Angkor Air t/a Cambodia Angkor Air Co., Ltd.","count":13},
{"airline":"Cameroon Airlines Corporation (Camair-Co)","count":18},
{"airline":"Caribbean Airlines Limited","count":13},
{"airline":"Carpatair S.A.","count":18},
{"airline":"Cayman Airways Limited","count":13},
{"airline":"China Airlines","count":1},
{"airline":"China Eastern Airlines","count":4},
{"airline":"Compagnie Aerienne ASKY dba ASKY","count":13},
{"airline":"Compania Mexicana de Aviacion S.A. de C.V.","count":13},
{"airline":"Compania Panamena de Aviacion, S.A. (COPA)","count":13},
{"airline":"Condor Flugdienst GmbH","count":13},
{"airline":"Corsair t/a Corsair International","count":13},
{"airline":"Croatia Airlines","count":13},
{"airline":"Cubana de Aviacion S.A.","count":13},
{"airline":"Cyprus Airways Limited","count":11},
{"airline":"Czech Airlines a.s,. CSA","count":12},
{"airline":"Darwin Airline SA","count":13},
{"airline":"Dniproavia  - Joint Stock Aviation Co.","count":15},
{"airline":"EVA Airways Corporation","count":1},
{"airline":"Edelweiss Air AG","count":2},
{"airline":"Egyptair","count":3},
{"airline":"El Al Israel Airlines Ltd.","count":3},
{"airline":"Estonian Air","count":18},
{"airline":"EuroLot S.A.","count":7},
{"airline":"Federal Airlines (Pty) Ltd","count":18},
{"airline":"Finnair Oyj","count":1},
{"airline":"Five Fourty Aviation Limited","count":13},
{"airline":"Fly Branson Travel dba Branson Air Express","count":18},
{"airline":"Flybe Limited","count":13},
{"airline":"Frontier Airlines, Inc.","count":13},
{"airline":"Garuda Indonesia","count":1},
{"airline":"Georgian Airways","count":15},
{"airline":"Groupe Air Senegal (Senegal Airlines)","count":18},
{"airline":"HG Aviation Limited dba Regent Airways","count":13},
{"airline":"Hahn Air Systems","count":5},
{"airline":"Hainan Airlines Company Limited","count":1},
{"airline":"Hawaiian Airlines, Inc.","count":10},
{"airline":"Hawkair Aviation Services Ltd.","count":13},
{"airline":"Hesa Airlines","count":7},
{"airline":"Hong Kong Airlines Limited","count":2},
{"airline":"Hong Kong Dragon Airlines Limited","count":2},
{"airline":"Hong Kong Express Airways Limited","count":7},
{"airline":"Horizon Air Industries, Inc.","count":13},
{"airline":"Hyannis Air Service, Inc. d/b/a Cape Air","count":13},
{"airline":"Icelandair","count":13},
{"airline":"Insel Air International B.V.","count":15},
{"airline":"Inter-Aviation Services dba Interair South Africa","count":18},
{"airline":"Israir Airlines and Tourism Ltd.","count":18},
{"airline":"JSC Air Lituanica","count":11},
{"airline":"JSC Aircompany SCAT","count":13},
{"airline":"Japan Airlines Co., Ltd.","count":1},
{"airline":"Japan Transocean Air Co. Ltd.","count":11},
{"airline":"Jat  Airways","count":13},
{"airline":"Jet Airways (India) Limited","count":1},
{"airline":"Jet Link Express Ltd.","count":13},
{"airline":"Jet Lite (India) Limited","count":7},
{"airline":"Jetblue Airways Corporation","count":13},
{"airline":"Job Air - Central Connect Airlines s.r.o","count":13},
{"airline":"Joint Stock Company Aircompany Yakutia","count":13},
{"airline":"Joint Stock Company Ural Airlines","count":18},
{"airline":"Joint- Stock Company Sakhalinskie Aviatrassy Airlines","count":18},
{"airline":"Joint-Stock Company Nordavia - regional airlines","count":13},
{"airline":"Joint-Stock Company Yamal Airlines","count":13},
{"airline":"Juneyao Airlines Co,. Ltd.","count":15},
{"airline":"KLM Royal Dutch Airlines","count":6},
{"airline":"Kam Air","count":13},
{"airline":"Korean Air Lines Co. Ltd.","count":1},
{"airline":"Kuwait Airways","count":1},
{"airline":"LAC Linea Aerea Cuencana","count":13},
{"airline":"LAM - Linhas Aereas de Mocambique","count":15},
{"airline":"LATAM Airlines Group S.A. dba LAN Airlines","count":12},
{"airline":"LIAT (1974) Ltd.","count":15},
{"airline":"LOT - Polish Airlines","count":13},
{"airline":"Lan Argentina","count":15},
{"airline":"Lan Ecuador - Aerolane Lineas Aereas Nacionales de Ecuador S.A.","count":15},
{"airline":"Lan Peru S.A.","count":15},
{"airline":"Lao Airlines","count":11},
{"airline":"Lineas Aereas Costarricenses S.A. (LACSA)","count":13},
{"airline":"Luxair","count":13},
{"airline":"MASwings SDN BHD","count":9},
{"airline":"MIAT - Mongolian Airlines","count":11},
{"airline":"MN Airlines LLC","count":13},
{"airline":"Mahan Airlines","count":5},
{"airline":"Malmo Aviation","count":18},
{"airline":"Mandarin Airlines Ltd.","count":11},
{"airline":"Marsland Aviation Co.","count":13},
{"airline":"Meridiana African Airlines (U) Limited dba Air Uganda","count":15},
{"airline":"Meridiana fly S.p.A.","count":9},
{"airline":"Mesa Airlines, Inc.","count":13},
{"airline":"Middle East Airlines AirLiban","count":11},
{"airline":"Moldavian Airlines","count":18},
{"airline":"Montenegro Airlines","count":13},
{"airline":"Multi-Aero, Inc. dba Air Choice One","count":15},
{"airline":"Myanmar Airways International Co., Ltd.","count":14},
{"airline":"NIKI  Luftfahrt GmbH","count":16},
{"airline":"Nature Air S.A.","count":18},
{"airline":"Nesma Airlines","count":7},
{"airline":"OJSC Aircompany Tatarstan","count":18},
{"airline":"Olympic Air","count":13},
{"airline":"Oman Air (S.A.O.C)","count":4},
{"airline":"PT. Batik Air Indonesia","count":7},
{"airline":"Pacific Wings, L.L.C.","count":10},
{"airline":"Pakistan International Airlines","count":1},
{"airline":"Philippine Airlines, Inc.","count":1},
{"airline":"Precision Air Services Ltd.","count":13},
{"airline":"Proflight Commuter Services LTD","count":13},
{"airline":"Qeshm Air","count":13},
{"airline":"Rossiya Airlines Open Joint Stock Company","count":17},
{"airline":"Rotana Jet Aviation dba Rotana Jet","count":1},
{"airline":"Royal Air Maroc","count":10},
{"airline":"Royal Jordanian (Alia - The Royal Jordanian Airline)","count":1},
{"airline":"RwandAir  Limited","count":13},
{"airline":"SATA - Air Acores","count":18},
{"airline":"SATA International Servicos e Transportes Aereos S.A.","count":13},
{"airline":"SWISS International Air Lines Ltd dba SWISS","count":1},
{"airline":"Safi Airways Ltd.","count":8},
{"airline":"Santa Barbara Airlines C.A.","count":13},
{"airline":"Saudi Arabian Airlines","count":1},
{"airline":"Scoot Private Limited","count":13},
{"airline":"Severstal Aircompany Ltd","count":13},
{"airline":"Shandong Airlines","count":12},
{"airline":"Shanghai Airlines Co. Ltd.","count":8},
{"airline":"Shenzhen Airlines","count":10},
{"airline":"Siberia Airlines","count":8},
{"airline":"SilkAir (S) Pte. Ltd.","count":7},
{"airline":"Silver Airways Corp","count":2},
{"airline":"Sky Airline S.A.","count":18},
{"airline":"Sky Bishek","count":13},
{"airline":"Sky Jet M.G. Inc.","count":13},
{"airline":"Solomon Airlines","count":13},
{"airline":"South East Asian Airlines","count":11},
{"airline":"SunExpress","count":13},
{"airline":"Surinam Airways Ltd.","count":13},
{"airline":"Sylt Air GmbH","count":13},
{"airline":"TAM - Transportes Aereos del Mercosur S.A.","count":18},
{"airline":"TAM Linhas Aereas S.A.","count":11},
{"airline":"TAME Linea Aerea del Ecuador","count":13},
{"airline":"TAROM - Transporturile Aeriene Romane S.A.","count":15},
{"airline":"TRIP Transporte Aereos Regionais Do Interior Paulista Ltda.","count":13},
{"airline":"TUI Airlines Nederland B.V.","count":18},
{"airline":"Taca International Airlines, S.A.","count":13},
{"airline":"Tiara Air N.V. dba Tiara Air Aruba","count":13},
{"airline":"Toumai Air Tchad","count":13},
{"airline":"Tradewind Aviation, LLC","count":18},
{"airline":"Transaero Airlines","count":7},
{"airline":"Transportes Aereos de Cabo Verde","count":15},
{"airline":"Transportes Aeromar, S.A. de C.V.","count":15},
{"airline":"Travel Service, A.S.","count":18},
{"airline":"Tunisair","count":13},
{"airline":"UNI Airways Corporation","count":10},
{"airline":"UTair Aviation Joint-Stock Company","count":13},
{"airline":"Ukraine International Airlines","count":6},
{"airline":"Uzbekistan Airways","count":13},
{"airline":"VIM Airlines","count":13},
{"airline":"VRG Linhas Aereas S.A.","count":15},
{"airline":"Vieques Air Link, Inc","count":13},
{"airline":"Vietnam Airlines Corporation","count":1},
{"airline":"Villa Air Pvt. Ltd. dba Villa Air","count":2},
{"airline":"Virgin America Inc.","count":13},
{"airline":"Virgin Atlantic Airways Limited","count":6},
{"airline":"Virgin Australia International Airlines Pty Ltd","count":11},
{"airline":"Vladivostok Air JSC","count":12},
{"airline":"Volotea, S.L.","count":13},
{"airline":"Vueling Airlines S.A.","count":13},
{"airline":"WESTbahn Management GmbH","count":13},
{"airline":"Welcome Air Luftfahrt Gmbh & Co KG","count":13},
{"airline":"WestJet","count":13},
{"airline":"Wind Rose Aviation Company","count":13},
{"airline":"Windward Islands Airways Int'l  N.V.","count":15},
{"airline":"Xiamen Airlines","count":12},
{"airline":"Yemenia - Yemen Airways","count":8},
{"airline":"flydubai","count":12}

		]
	return json.dumps(data)
	pass

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


