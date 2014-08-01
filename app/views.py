
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
{"airline":"A6","count":358,"airline_name":"AAA - Air Alps Aviation"},
{"airline":"K4","count":126,"airline_name":"ALS Ltd."},
{"airline":"EH","count":231,"airline_name":"ANA Wings Co., Ltd."},
{"airline":"GU","count":1048,"airline_name":"AVIATECA, S.A."},
{"airline":"JP","count":5491,"airline_name":"Adria Airways - The Airline of Slovenia"},
{"airline":"A3","count":4193,"airline_name":"Aegean Airlines S.A."},
{"airline":"EI","count":1742,"airline_name":"Aer Lingus Limited"},
{"airline":"S9","count":126,"airline_name":"Aero Surveys Ltd  t/a  Starbow"},
{"airline":"SU","count":7334,"airline_name":"Aeroflot Russian Airlines"},
{"airline":"AR","count":4736,"airline_name":"Aerolineas Argentinas S.A."},
{"airline":"2K","count":210,"airline_name":"Aerolineas Galapagos S.A. Aerogal"},
{"airline":"AM","count":3670,"airline_name":"Aeromexico Aerovias de Mexico S.A. de C.V."},
{"airline":"OT","count":126,"airline_name":"Aeropelican Air Services Pty Ltd"},
{"airline":"VV","count":714,"airline_name":"Aerosvit Airlines"},
{"airline":"AV","count":6225,"airline_name":"Aerovias del Continente Americano S.A AVIANCA"},
{"airline":"8U","count":463,"airline_name":"Afriqiyah Airways"},
{"airline":"ZI","count":230,"airline_name":"Aigle Azur"},
{"airline":"AH","count":3753,"airline_name":"Air Algerie"},
{"airline":"E5","count":357,"airline_name":"Air Arabia Egypt"},
{"airline":"KC","count":3899,"airline_name":"Air Astana"},
{"airline":"UU","count":2032,"airline_name":"Air Austral"},
{"airline":"BT","count":3981,"airline_name":"Air Baltic Corporation AS"},
{"airline":"AB","count":4908,"airline_name":"Air Berlin PLC & Co. Luftverkehrs KG"},
{"airline":"BP","count":3563,"airline_name":"Air Botswana"},
{"airline":"2J","count":904,"airline_name":"Air Burkina"},
{"airline":"SB","count":3187,"airline_name":"Air Caledonie International"},
{"airline":"AC","count":4657,"airline_name":"Air Canada"},
{"airline":"TX","count":461,"airline_name":"Air Caraibes"},
{"airline":"UY","count":1275,"airline_name":"Air Caucasus"},
{"airline":"CA","count":8046,"airline_name":"Air China Limited"},
{"airline":"XK","count":1047,"airline_name":"Air Corsica"},
{"airline":"YN","count":126,"airline_name":"Air Creebec (1994) Inc."},
{"airline":"EN","count":504,"airline_name":"Air Dolomiti S.p.A. Aeree Regionali Europee"},
{"airline":"UX","count":5741,"airline_name":"Air Europa Lineas Aereas, S.A."},
{"airline":"AF","count":7318,"airline_name":"Air France"},
{"airline":"ZX","count":126,"airline_name":"Air Georgian Ltd. dba Air Alliance"},
{"airline":"AI","count":5803,"airline_name":"Air India Limited"},
{"airline":"I9","count":251,"airline_name":"Air Italy S.p.A."},
{"airline":"NQ","count":126,"airline_name":"Air Japan Company Ltd."},
{"airline":"T3","count":126,"airline_name":"Air Kilroe Limited t/a Eastern Airways"},
{"airline":"JS","count":378,"airline_name":"Air Koryo"},
{"airline":"NX","count":3391,"airline_name":"Air Macau Company Limited"},
{"airline":"MD","count":3666,"airline_name":"Air Madagascar"},
{"airline":"QM","count":1947,"airline_name":"Air Malawi Limited"},
{"airline":"KM","count":6076,"airline_name":"Air Malta p.l.c."},
{"airline":"6T","count":125,"airline_name":"Air Mandalay Ltd."},
{"airline":"MK","count":5993,"airline_name":"Air Mauritius"},
{"airline":"ML","count":126,"airline_name":"Air Mediterranee"},
{"airline":"9U","count":2637,"airline_name":"Air Moldova"},
{"airline":"SW","count":4276,"airline_name":"Air Namibia"},
{"airline":"NZ","count":4908,"airline_name":"Air New Zealand Limited"},
{"airline":"PX","count":4900,"airline_name":"Air Niugini Pty Limited dba Air Niugini"},
{"airline":"YW","count":251,"airline_name":"Air Nostrum L.A.M.S.A."},
{"airline":"FJ","count":4676,"airline_name":"Air Pacific Limited t/a Fiji Airways"},
{"airline":"7P","count":231,"airline_name":"Air Panama dba Parsa, S.A."},
{"airline":"PJ","count":126,"airline_name":"Air Saint  Pierre"},
{"airline":"HM","count":4923,"airline_name":"Air Seychelles Limited"},
{"airline":"VT","count":1070,"airline_name":"Air Tahiti"},
{"airline":"TN","count":3252,"airline_name":"Air Tahiti Nui"},
{"airline":"TS","count":211,"airline_name":"Air Transat"},
{"airline":"NF","count":1358,"airline_name":"Air Vanuatu (Operations) Limited"},
{"airline":"ZW","count":482,"airline_name":"Air Wisconsin Airlines Corporation (AWAC)"},
{"airline":"UM","count":252,"airline_name":"Air Zimbabwe (Pvt) Ltd."},
{"airline":"SZ","count":251,"airline_name":"Aircompany Somon Air LLC"},
{"airline":"QU","count":210,"airline_name":"Airline Utair - Ukraine"},
{"airline":"CG","count":126,"airline_name":"Airlines of Papua New Guinea Limited"},
{"airline":"AS","count":3232,"airline_name":"Alaska Airlines Inc."},
{"airline":"CT","count":126,"airline_name":"Alitalia CityLiner S.p.A."},
{"airline":"AZ","count":7798,"airline_name":"Alitalia-Compagnia Aerea Italiana S.p.A"},
{"airline":"NH","count":5475,"airline_name":"All Nippon Airways Co. Ltd."},
{"airline":"N6","count":355,"airline_name":"Alpine Air Pvt. Ltd."},
{"airline":"AA","count":5264,"airline_name":"American Airlines Inc."},
{"airline":"FG","count":376,"airline_name":"Ariana Afghan Airlines"},
{"airline":"W3","count":483,"airline_name":"Arik Air Limited"},
{"airline":"IZ","count":1971,"airline_name":"Arkia - Israeli Airlines Ltd"},
{"airline":"U8","count":1213,"airline_name":"Armavia"},
{"airline":"R7","count":357,"airline_name":"Aserca Airlines, C.A."},
{"airline":"OZ","count":7273,"airline_name":"Asiana Airlines Inc."},
{"airline":"TD","count":125,"airline_name":"Atlantis European Airways"},
{"airline":"KK","count":2663,"airline_name":"Atlasjet Airlines Inc."},
{"airline":"IQ","count":376,"airline_name":"Augsburg Airways GmbH"},
{"airline":"OS","count":5618,"airline_name":"Austrian Airlines AG dba Austrian"},
{"airline":"J2","count":1758,"airline_name":"Azerbaijan Hava Yollary"},
{"airline":"CJ","count":378,"airline_name":"BA Cityflyer Limited"},
{"airline":"UP","count":838,"airline_name":"Bahamasair Holdings, Limited"},
{"airline":"PG","count":3749,"airline_name":"Bangkok Airways Public Company Limited"},
{"airline":"JV","count":251,"airline_name":"Bearskin Lake air services LP"},
{"airline":"JD","count":1550,"airline_name":"Beijing Capital Airlines Co. Ltd."},
{"airline":"B2","count":1716,"airline_name":"Belavia"},
{"airline":"LZ","count":691,"airline_name":"Belle Air Company"},
{"airline":"J8","count":376,"airline_name":"Berjaya Air Sdn. Bhd."},
{"airline":"BG","count":1991,"airline_name":"Biman Bangladesh Airlines"},
{"airline":"BV","count":1465,"airline_name":"Blue Panorama Airlines S.p.A."},
{"airline":"DC","count":211,"airline_name":"Braathens Regional AB"},
{"airline":"7F","count":483,"airline_name":"Bradley Air Services Limited t/a First Air"},
{"airline":"FQ","count":126,"airline_name":"Brindabella Airlines Pty. Ltd."},
{"airline":"BA","count":7316,"airline_name":"British Airways p.l.c."},
{"airline":"BD","count":4086,"airline_name":"British Midland Airways Ltd. dba bmi"},
{"airline":"BM","count":126,"airline_name":"British Midland Regional Limited t/a bmi Regional"},
{"airline":"SN","count":7338,"airline_name":"Brussels Airlines N.V."},
{"airline":"FB","count":2557,"airline_name":"Bulgaria Air"},
{"airline":"XM","count":3270,"airline_name":"C.A.I. First S.p.A."},
{"airline":"VE","count":1069,"airline_name":"C.A.I. Second S.p.A."},
{"airline":"3S","count":336,"airline_name":"CAIRE dba Air Antilles Express"},
{"airline":"9Q","count":126,"airline_name":"Caicos Express Airways"},
{"airline":"K6","count":126,"airline_name":"Cambodia Angkor Air t/a Cambodia Angkor Air Co., Ltd."},
{"airline":"5T","count":693,"airline_name":"Canadian North Inc."},
{"airline":"TL","count":126,"airline_name":"Capiteq Limited dba AIRNORTH"},
{"airline":"BW","count":1890,"airline_name":"Caribbean Airlines Limited"},
{"airline":"V3","count":1531,"airline_name":"Carpatair S.A."},
{"airline":"CX","count":7356,"airline_name":"Cathay Pacific Airways Ltd."},
{"airline":"KX","count":1678,"airline_name":"Cayman Airways Limited"},
{"airline":"9M","count":231,"airline_name":"Central Mountain Air Ltd."},
{"airline":"CE","count":126,"airline_name":"Chalair Aviation"},
{"airline":"CI","count":8110,"airline_name":"China Airlines"},
{"airline":"MU","count":6580,"airline_name":"China Eastern Airlines"},
{"airline":"CZ","count":7211,"airline_name":"China Southern Airlines"},
{"airline":"CW","count":815,"airline_name":"Chinggis Airways LLC"},
{"airline":"OQ","count":125,"airline_name":"Chongqing Airlines Co. Ltd"},
{"airline":"AU","count":461,"airline_name":"Cielos del Sur S.A. dba Austral Lineas Aereas S.A."},
{"airline":"E8","count":355,"airline_name":"City Airways Company Limited dba City Airways"},
{"airline":"MN","count":252,"airline_name":"Comair Ltd."},
{"airline":"KP","count":526,"airline_name":"Compagnie Aerienne ASKY dba ASKY"},
{"airline":"BU","count":2680,"airline_name":"Compagnie Africaine d'Aviation CAA"},
{"airline":"MX","count":3146,"airline_name":"Compania Mexicana de Aviacion S.A. de C.V."},
{"airline":"CM","count":3589,"airline_name":"Compania Panamena de Aviacion, S.A. (COPA)"},
{"airline":"CP","count":105,"airline_name":"Compass Airlines Inc."},
{"airline":"DE","count":1214,"airline_name":"Condor Flugdienst GmbH"},
{"airline":"CS","count":629,"airline_name":"Continental Micronesia, Inc."},
{"airline":"SS","count":1697,"airline_name":"Corsair t/a Corsair International"},
{"airline":"OU","count":5849,"airline_name":"Croatia Airlines"},
{"airline":"CU","count":5134,"airline_name":"Cubana de Aviacion S.A."},
{"airline":"CY","count":4231,"airline_name":"Cyprus Airways Limited"},
{"airline":"OK","count":7546,"airline_name":"Czech Airlines a.s,. CSA"},
{"airline":"D3","count":483,"airline_name":"Daallo Airlines"},
{"airline":"DX","count":125,"airline_name":"Danish Air Transport"},
{"airline":"F7","count":1236,"airline_name":"Darwin Airline SA"},
{"airline":"DL","count":7945,"airline_name":"Delta Air Lines Inc."},
{"airline":"LH","count":6435,"airline_name":"Deutsche Lufthansa AG"},
{"airline":"Z6","count":1380,"airline_name":"Dniproavia  - Joint Stock Aviation Co."},
{"airline":"KB","count":126,"airline_name":"Druk Air Corporation Ltd."},
{"airline":"ZE","count":1,"airline_name":"EASTAR JET Co. Ltd."},
{"airline":"BR","count":7333,"airline_name":"EVA Airways Corporation"},
{"airline":"MS","count":6207,"airline_name":"Egyptair"},
{"airline":"LY","count":6501,"airline_name":"El Al Israel Airlines Ltd."},
{"airline":"EK","count":6936,"airline_name":"Emirates"},
{"airline":"7H","count":357,"airline_name":"Era Aviation, Inc."},
{"airline":"B8","count":627,"airline_name":"Eritrean Airlines"},
{"airline":"E4","count":125,"airline_name":"Estelar Latinoamerica C.A."},
{"airline":"OV","count":4735,"airline_name":"Estonian Air"},
{"airline":"ET","count":7212,"airline_name":"Ethiopian Airlines Enterprise"},
{"airline":"EY","count":6979,"airline_name":"Etihad Airways"},
{"airline":"K2","count":125,"airline_name":"EuroLot S.A."},
{"airline":"EW","count":3038,"airline_name":"Eurowings GmbH"},
{"airline":"X7","count":126,"airline_name":"Exec Air, Inc. of Naples"},
{"airline":"AY","count":6600,"airline_name":"Finnair Oyj"},
{"airline":"W2","count":315,"airline_name":"FlexFlight ApS"},
{"airline":"9Y","count":126,"airline_name":"Fly Georgia"},
{"airline":"XN","count":357,"airline_name":"Fly Logic Malmo AB"},
{"airline":"BE","count":4654,"airline_name":"Flybe Limited"},
{"airline":"Z7","count":125,"airline_name":"Freshair-NU-Aero (Pvt) Ltd"},
{"airline":"F9","count":839,"airline_name":"Frontier Airlines, Inc."},
{"airline":"GA","count":5091,"airline_name":"Garuda Indonesia"},
{"airline":"A9","count":2431,"airline_name":"Georgian Airways"},
{"airline":"4U","count":358,"airline_name":"Germanwings GmbH"},
{"airline":"YR","count":483,"airline_name":"Grand Canyon Airlines, Inc. dba Scenic Airlines"},
{"airline":"ZK","count":461,"airline_name":"Great Lakes Aviation Ltd."},
{"airline":"DN","count":336,"airline_name":"Groupe Air Senegal (Senegal Airlines)"},
{"airline":"GF","count":5889,"airline_name":"Gulf Air B.S.C. (c)"},
{"airline":"A5","count":252,"airline_name":"HOP!"},
{"airline":"HR","count":8638,"airline_name":"Hahn Air Lines"},
{"airline":"HU","count":6096,"airline_name":"Hainan Airlines Company Limited"},
{"airline":"WP","count":483,"airline_name":"Hawaii Island Air, Inc. dba Island Air"},
{"airline":"HA","count":1827,"airline_name":"Hawaiian Airlines, Inc."},
{"airline":"NS","count":125,"airline_name":"Hebei Airlines Co., Ltd."},
{"airline":"YO","count":3877,"airline_name":"Heli Air Monaco"},
{"airline":"H4","count":125,"airline_name":"Heli Securite Helicopter Airline"},
{"airline":"UD","count":252,"airline_name":"Hex'Air"},
{"airline":"HX","count":4018,"airline_name":"Hong Kong Airlines Limited"},
{"airline":"KA","count":5849,"airline_name":"Hong Kong Dragon Airlines Limited"},
{"airline":"UO","count":252,"airline_name":"Hong Kong Express Airways Limited"},
{"airline":"QX","count":126,"airline_name":"Horizon Air Industries, Inc."},
{"airline":"9K","count":252,"airline_name":"Hyannis Air Service, Inc. d/b/a Cape Air"},
{"airline":"IB","count":5389,"airline_name":"Iberia Lineas Aereas de Espana S.A. Operadora"},
{"airline":"FI","count":6371,"airline_name":"Icelandair"},
{"airline":"7I","count":336,"airline_name":"Insel Air International B.V."},
{"airline":"8I","count":105,"airline_name":"InselAir Aruba N.V. dba InselAir Aruba"},
{"airline":"D6","count":2831,"airline_name":"Inter-Aviation Services dba Interair South Africa"},
{"airline":"IR","count":3835,"airline_name":"Iran Air The Airline of Islamic Republic of Iran"},
{"airline":"EP","count":126,"airline_name":"Iran Aseman Airlines"},
{"airline":"WC","count":105,"airline_name":"Islena de Inversiones S.A. de C.V. dba Islena Airlines"},
{"airline":"6H","count":731,"airline_name":"Israir Airlines and Tourism Ltd."},
{"airline":"JC","count":861,"airline_name":"JAL Express"},
{"airline":"DV","count":125,"airline_name":"JSC Aircompany SCAT"},
{"airline":"Z9","count":356,"airline_name":"JSC Bek Air"},
{"airline":"IH","count":105,"airline_name":"JSC Aircompany Irtysh-Air"},
{"airline":"D9","count":501,"airline_name":"JSC DONAVIA"},
{"airline":"JL","count":7650,"airline_name":"Japan Airlines Co., Ltd."},
{"airline":"NU","count":1615,"airline_name":"Japan Transocean Air Co. Ltd."},
{"airline":"JU","count":4484,"airline_name":"Jat  Airways"},
{"airline":"QK","count":126,"airline_name":"Jazz Aviation LP"},
{"airline":"9W","count":8804,"airline_name":"Jet Airways (India) Limited"},
{"airline":"S2","count":2199,"airline_name":"Jet Lite (India) Limited"},
{"airline":"B6","count":1468,"airline_name":"Jetblue Airways Corporation"},
{"airline":"JQ","count":2348,"airline_name":"Jetstar Airways Pty Limited"},
{"airline":"3K","count":1006,"airline_name":"Jetstar Asia Airways Pte Ltd"},
{"airline":"GK","count":1258,"airline_name":"Jetstar Japan Co., Ltd."},
{"airline":"BL","count":881,"airline_name":"Jetstar Pacific Airlines"},
{"airline":"R2","count":126,"airline_name":"Joint Stock Company Orenburg airlines dba ORENAIR"},
{"airline":"U6","count":2117,"airline_name":"Joint Stock Company Ural Airlines"},
{"airline":"HZ","count":378,"airline_name":"Joint- Stock Company Sakhalinskie Aviatrassy Airlines"},
{"airline":"5N","count":126,"airline_name":"Joint-Stock Company Nordavia - regional airlines"},
{"airline":"JR","count":252,"airline_name":"Joy Air"},
{"airline":"HO","count":378,"airline_name":"Juneyao Airlines Co,. Ltd."},
{"airline":"WA","count":3037,"airline_name":"KLM Cityhopper"},
{"airline":"KL","count":7964,"airline_name":"KLM Royal Dutch Airlines"},
{"airline":"KQ","count":6540,"airline_name":"Kenya Airways"},
{"airline":"KE","count":7585,"airline_name":"Korean Air Lines Co. Ltd."},
{"airline":"ZC","count":230,"airline_name":"Korongo Airlines"},
{"airline":"KU","count":5533,"airline_name":"Kuwait Airways"},
{"airline":"TM","count":1802,"airline_name":"LAM - Linhas Aereas de Mocambique"},
{"airline":"LA","count":3840,"airline_name":"LATAM Airlines Group S.A. dba LAN Airlines"},
{"airline":"LI","count":2117,"airline_name":"LIAT (1974) Ltd."},
{"airline":"LO","count":5157,"airline_name":"LOT - Polish Airlines"},
{"airline":"4M","count":3610,"airline_name":"Lan Argentina"},
{"airline":"XL","count":3736,"airline_name":"Lan Ecuador - Aerolane Lineas Aereas Nacionales de Ecuador S.A."},
{"airline":"LP","count":3610,"airline_name":"Lan Peru S.A."},
{"airline":"QV","count":1363,"airline_name":"Lao Airlines"},
{"airline":"QL","count":125,"airline_name":"Linea Aerea de Servicio Ejecutivo Regional Laser C.A"},
{"airline":"LR","count":3945,"airline_name":"Lineas Aereas Costarricenses S.A. (LACSA)"},
{"airline":"CL","count":587,"airline_name":"Lufthansa CityLine GmbH"},
{"airline":"LG","count":5805,"airline_name":"Luxair"},
{"airline":"OM","count":2011,"airline_name":"MIAT - Mongolian Airlines"},
{"airline":"SY","count":105,"airline_name":"MN Airlines LLC"},
{"airline":"VM","count":231,"airline_name":"Macair Jet S.A."},
{"airline":"W5","count":731,"airline_name":"Mahan Airlines"},
{"airline":"MH","count":7860,"airline_name":"Malaysia  Airline System Berhad"},
{"airline":"TF","count":1175,"airline_name":"Malmo Aviation"},
{"airline":"AE","count":4063,"airline_name":"Mandarin Airlines Ltd."},
{"airline":"JE","count":1047,"airline_name":"Mango Airlines (Pty) Ltd trading as MANGO"},
{"airline":"L6","count":125,"airline_name":"Mauritanian Airlines International"},
{"airline":"U7","count":337,"airline_name":"Meridiana African Airlines (U) Limited dba Air Uganda"},
{"airline":"IG","count":4127,"airline_name":"Meridiana fly S.p.A."},
{"airline":"YV","count":609,"airline_name":"Mesa Airlines, Inc."},
{"airline":"ME","count":5975,"airline_name":"Middle East Airlines AirLiban"},
{"airline":"2M","count":837,"airline_name":"Moldavian Airlines"},
{"airline":"YM","count":2180,"airline_name":"Montenegro Airlines"},
{"airline":"3E","count":20,"airline_name":"Multi-Aero, Inc. dba Air Choice One"},
{"airline":"8M","count":1780,"airline_name":"Myanmar Airways International Co., Ltd."},
{"airline":"HG","count":1593,"airline_name":"NIKI  Luftfahrt GmbH"},
{"airline":"N8","count":20,"airline_name":"National Air Cargo Group, Inc. dba National Airlines"},
{"airline":"ON","count":105,"airline_name":"Nauru Air Corporation t/a Our Airline"},
{"airline":"RA","count":3313,"airline_name":"Nepal Airlines Corporation"},
{"airline":"U9","count":376,"airline_name":"OJSC Aircompany Tatarstan"},
{"airline":"O6","count":356,"airline_name":"Oceanair Linhas Aereas Ltda."},
{"airline":"OA","count":5302,"airline_name":"Olympic Air"},
{"airline":"WY","count":4654,"airline_name":"Oman Air (S.A.O.C)"},
{"airline":"EC","count":126,"airline_name":"Openskies"},
{"airline":"OX","count":126,"airline_name":"Orient Thai Airlines"},
{"airline":"LW","count":1633,"airline_name":"Pacific Wings, L.L.C."},
{"airline":"PK","count":4236,"airline_name":"Pakistan International Airlines"},
{"airline":"PC","count":125,"airline_name":"Pegasus Hava Tasimaciligi A.S."},
{"airline":"KS","count":126,"airline_name":"Penair"},
{"airline":"DP","count":460,"airline_name":"Perla Airlines, C.A."},
{"airline":"9P","count":126,"airline_name":"Petra Airlines/Zuwar Investments Co. dba Petra Airlines"},
{"airline":"PR","count":4503,"airline_name":"Philippine Airlines, Inc."},
{"airline":"PI","count":125,"airline_name":"Polar Airlines OJSC"},
{"airline":"PD","count":125,"airline_name":"Porter Airlines Inc."},
{"airline":"PW","count":1428,"airline_name":"Precision Air Services Ltd."},
{"airline":"PB","count":210,"airline_name":"Provincial Airlines"},
{"airline":"ZR","count":941,"airline_name":"Punto Azul"},
{"airline":"QF","count":7440,"airline_name":"Qantas Airways Ltd."},
{"airline":"QR","count":7755,"airline_name":"Qatar Airways(Q.C.S.C)"},
{"airline":"YX","count":251,"airline_name":"Republic Airline Inc.."},
{"airline":"FV","count":3691,"airline_name":"Rossiya Airlines Open Joint Stock Company"},
{"airline":"AT","count":5239,"airline_name":"Royal Air Maroc"},
{"airline":"BI","count":5004,"airline_name":"Royal Brunei Airlines Sdn. Bhd."},
{"airline":"RJ","count":7818,"airline_name":"Royal Jordanian (Alia - The Royal Jordanian Airline)"},
{"airline":"WB","count":924,"airline_name":"RwandAir  Limited"},
{"airline":"SP","count":1068,"airline_name":"SATA - Air Acores"},
{"airline":"S4","count":1172,"airline_name":"SATA International Servicos e Transportes Aereos S.A."},
{"airline":"LX","count":6333,"airline_name":"SWISS International Air Lines Ltd dba SWISS"},
{"airline":"4Q","count":629,"airline_name":"Safi Airways Ltd."},
{"airline":"S3","count":482,"airline_name":"Santa Barbara Airlines C.A."},
{"airline":"SV","count":6936,"airline_name":"Saudi Arabian Airlines"},
{"airline":"SK","count":5534,"airline_name":"Scandinavian Airlines System (SAS)"},
{"airline":"BB","count":126,"airline_name":"Seaborne  Airlines"},
{"airline":"NL","count":377,"airline_name":"Shaheen Air International"},
{"airline":"SC","count":1531,"airline_name":"Shandong Airlines"},
{"airline":"FM","count":4442,"airline_name":"Shanghai Airlines Co. Ltd."},
{"airline":"ZH","count":2894,"airline_name":"Shenzhen Airlines"},
{"airline":"S7","count":3792,"airline_name":"Siberia Airlines"},
{"airline":"3U","count":882,"airline_name":"Sichuan Airlines Co. Ltd."},
{"airline":"ZY","count":251,"airline_name":"Sik-Ay Hava Tasimacilik A.S. (Sky Airlines)"},
{"airline":"MI","count":3394,"airline_name":"SilkAir (S) Pte. Ltd."},
{"airline":"3M","count":252,"airline_name":"Silver Airways Corp"},
{"airline":"SQ","count":7020,"airline_name":"Singapore Airlines Limited"},
{"airline":"H2","count":798,"airline_name":"Sky Airline S.A."},
{"airline":"OO","count":587,"airline_name":"SkyWest  Airlines"},
{"airline":"IE","count":2241,"airline_name":"Solomon Airlines"},
{"airline":"SA","count":7254,"airline_name":"South African Airways"},
{"airline":"XO","count":126,"airline_name":"South East Asian Airlines (SEAIR) International, Inc."},
{"airline":"PL","count":230,"airline_name":"Southern Air Charter Co., Limited"},
{"airline":"UL","count":6497,"airline_name":"SriLankan Airlines Limited"},
{"airline":"SD","count":504,"airline_name":"Sudan Airways Co. Ltd."},
{"airline":"2U","count":125,"airline_name":"Sun d'Or International Airlines"},
{"airline":"PY","count":1613,"airline_name":"Surinam Airways Ltd."},
{"airline":"RB","count":1801,"airline_name":"Syrian Arab Airlines"},
{"airline":"DT","count":3042,"airline_name":"TAAG - Linhas Aereas de Angola (Angola Airlines)"},
{"airline":"PZ","count":5953,"airline_name":"TAM - Transportes Aereos del Mercosur S.A."},
{"airline":"JJ","count":6185,"airline_name":"TAM Linhas Aereas S.A."},
{"airline":"EQ","count":691,"airline_name":"TAME Linea Aerea del Ecuador"},
{"airline":"TP","count":7422,"airline_name":"TAP Portugal"},
{"airline":"RO","count":5803,"airline_name":"TAROM - Transporturile Aeriene Romane S.A."},
{"airline":"TA","count":3945,"airline_name":"Taca International Airlines, S.A."},
{"airline":"4E","count":105,"airline_name":"Tanana Air Service"},
{"airline":"TG","count":7019,"airline_name":"Thai Airways International Public Company Ltd."},
{"airline":"TT","count":230,"airline_name":"Tiger Airways Australia"},
{"airline":"T0","count":3567,"airline_name":"Trans American Airlines, S.A. TACA PERU"},
{"airline":"AX","count":1423,"airline_name":"Trans States Airlines, LLC"},
{"airline":"GE","count":2032,"airline_name":"TransAsia Airways Corporation"},
{"airline":"UN","count":4443,"airline_name":"Transaero Airlines"},
{"airline":"TO","count":20,"airline_name":"Transavia France"},
{"airline":"VR","count":1740,"airline_name":"Transportes Aereos de Cabo Verde"},
{"airline":"VW","count":1300,"airline_name":"Transportes Aeromar, S.A. de C.V."},
{"airline":"QS","count":125,"airline_name":"Travel Service, A.S."},
{"airline":"9N","count":125,"airline_name":"Tropic Air Limited"},
{"airline":"TU","count":4256,"airline_name":"Tunisair"},
{"airline":"UG","count":482,"airline_name":"Tunisair Express"},
{"airline":"TK","count":7168,"airline_name":"Turkish Airlines Inc."},
{"airline":"T5","count":126,"airline_name":"Turkmenistan Airlines"},
{"airline":"T7","count":126,"airline_name":"Twin Jet"},
{"airline":"VO","count":1047,"airline_name":"Tyrolean Airways Tiroler Luftfahrt GmbH"},
{"airline":"B7","count":1779,"airline_name":"UNI Airways Corporation"},
{"airline":"US","count":7422,"airline_name":"US Airways, Inc."},
{"airline":"UT","count":1087,"airline_name":"UTair Aviation Joint-Stock Company"},
{"airline":"PS","count":4903,"airline_name":"Ukraine International Airlines"},
{"airline":"UA","count":6853,"airline_name":"United Airlines, Inc."},
{"airline":"HY","count":2723,"airline_name":"Uzbekistan Airways"},
{"airline":"G3","count":3415,"airline_name":"VRG Linhas Aereas S.A."},
{"airline":"VF","count":1006,"airline_name":"Valuair Ltd."},
{"airline":"VJ","count":125,"airline_name":"Vietjet Aviation Joint Stock Company (Vietjet Air)"},
{"airline":"VN","count":6453,"airline_name":"Vietnam Airlines Corporation"},
{"airline":"VP","count":1949,"airline_name":"Villa Air Pvt. Ltd. dba Villa Air"},
{"airline":"VX","count":1760,"airline_name":"Virgin America Inc."},
{"airline":"VS","count":5638,"airline_name":"Virgin Atlantic Airways Limited"},
{"airline":"VA","count":2198,"airline_name":"Virgin Australia International Airlines Pty Ltd"},
{"airline":"XF","count":1132,"airline_name":"Vladivostok Air JSC"},
{"airline":"WT","count":231,"airline_name":"Wasaya Airways"},
{"airline":"WH","count":860,"airline_name":"West African Airlines"},
{"airline":"WS","count":1992,"airline_name":"WestJet"},
{"airline":"WF","count":4801,"airline_name":"Wideroe's Flyveselskap A.S."},
{"airline":"WM","count":462,"airline_name":"Windward Islands Airways Int'l  N.V."},
{"airline":"MF","count":2642,"airline_name":"Xiamen Airlines"},
{"airline":"IY","count":2996,"airline_name":"Yemenia - Yemen Airways"},
{"airline":"FZ","count":378,"airline_name":"flydubai"},


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

@app.route("/getshs/<property>")
def get_shs(property):
	retrresults = models.get_shs(property)
	return render_template("shs.html", qresults=retrresults)		
