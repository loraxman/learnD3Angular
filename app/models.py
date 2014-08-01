'''
Created on Jan 28, 2014

@author: SG0166434
'''

from couchdb.mapping import (Document, IntegerField,ListField,FloatField, TextField, DictField, Mapping)
import couchdb
import custmodel
import pyodbc
from datetime import datetime

class Model(Document):
    
    name = TextField()
    
    
class Cat(Document):
    
    catname = TextField()
    models = ListField(DictField(Mapping.build(
            name = TextField(),
            columns = ListField(TextField())
            
            
            )))
    
   
   
def getall():
    couch = couchdb.Server("http://localhost:5984") # Assuming localhost:5984
    # If your CouchDB server is running elsewhere, set it up like this:
    cats = {}
    db = couch['metamodel']

    docs  = []
    for docid in db:
        m = db.get(docid)
        docs.append( m)
        
    return docs
def loaddb():
    couch = couchdb.Server("http://localhost:5984") # Assuming localhost:5984
    # If your CouchDB server is running elsewhere, set it up like this:
    cats = {}
    db = couch['metamodel']
    items = open("C:/proj/cats/tabs/res.csv").read()
    items = items.split("\n")
    md = {}
    for it in items:
        if len(it) < 4:
            break
        item  = it.split(",")
        #check to see if cat exists
        if not cats.has_key(item[0]):
            cats[item[0]] = Cat()
            cats[item[0]].catname = item[0]
            
        #check to see if model exists
        if  cats[item[0]].models == None:
            cats[item[0]].models = []
            
        #populate model if not there
        
        #find model
        found = False
        for n in cats[item[0]].models:
            if n['name'] == item[3]:
                 found = True
                 md = n
        
        if not found:
            md = {}
            md['name'] = item[3]
            md['columns'] = []
            cats[item[0]].models.append(md)
         
             
        md['columns'].append(item[1])
       # print md['columns']
        
    for cat in cats.keys():
        cats[cat].store(db)
   
    
    return cats 
         
    m = Cat()
    m.catname = 'TestCat'
    
    md = {}
    md['name']='Testmod'
    md['columns'] = []
    md['columns'].append("Key1")
    md['columns'].append("Key2")
    
    
    m.models['TestMod'].append(md)
    m.store(db)
    
    
def get_shs(property):
        
    qresults = {}
    #checked out
    conn=pyodbc.connect("DSN=VerticaDEV")
    cur = conn.cursor()
    sql = "SELECT COUNT(*)  FROM reservation WHERE departure = '2012-10-12' AND status = 102 AND property = '"  + property + "'"
    cur.execute(sql)
    checkouts = cur.fetchone()[0]
    
    qresults['checkouts']= checkouts
    
    sql = "  SELECT COUNT (*)  "\
            "FROM reservation r, reservation_info ri"\
           " WHERE r.status = 101 "\
           "  AND ri.walkin = 1 "\
            " and r.property= '" + property +  "'" \
           "  and r.property = ri.property "\
            " and r.ACCOUNT = ri.ACCOUNT "
          #  "  group by r.property; "
            
    cur.execute(sql)
    walkins = cur.fetchone()[0]
    
    qresults['walkins'] = walkins
    
    sql = "  SELECT COUNT (*)  "\
            "FROM reservation r, reservation_info ri"\
           " WHERE r.status = 101 "\
            " and r.property='"  + property + "' "\
           "  and r.property = ri.property "\
            " and r.ACCOUNT = ri.ACCOUNT "
          #  "  group by r.property; "
            
    cur.execute(sql)
    arrived = cur.fetchone()[0]
    qresults['arrived'] = arrived
    
    sql = "  SELECT COUNT (*)  "\
            "FROM reservation r, reservation_info ri"\
           " WHERE r.status = 102 "\
            " and r.property='"  + property + "' "\
           "  and r.property = ri.property "\
            " AND ri.earlydeparture = 1 "\
            " and r.ACCOUNT = ri.ACCOUNT "
          #  "  group by r.property; "
            
    cur.execute(sql)
    earlycheckout = cur.fetchone()[0]
    qresults['earlycheckout'] = earlycheckout
    
    totalguests = arrived +walkins + checkouts + earlycheckout
    
    sql =     "SELECT COUNT (*) "\
        "    FROM roomtype_rooms "\
         "  WHERE active = 1 AND property = '"  + property + "';"
            
    cur.execute(sql)
    totalrooms = cur.fetchone()[0]
    
    qresults['totalrooms']  = totalrooms
    
    
    sql =     "SELECT COUNT (*) "\
        "    FROM roomtype_rooms_ooo "\
         "  WHERE ooo_date = '2012-10-12' AND ooi = 1  and property = '"  + property + "';"
     
    cur.execute(sql)
    outorder = cur.fetchone()[0]
    qresults['outorder'] = outorder
    
    sql = "SELECT COUNT (*), sum(adult), sum(child1) + sum(child2)  "\
        "    FROM reservation "\
         "  WHERE departure > '2012-10-12' AND STATUS = 101 AND  property = '"  + property + "';"
     
    cur.execute(sql)
    stayover = cur.fetchone()[0]
    
    qresults['stayover'] = stayover
                
    sql = "SELECT  sum(adult) +  sum(child1) + sum(child2)  "\
        "    FROM reservation "\
         "  WHERE departure = '2012-10-12' AND STATUS = 101 AND  property = '"  + property + "';"
     
    cur.execute(sql)
    dueout = cur.fetchone()[0]
    if dueout == None:
        dueout = 1
    
    qresults['dueout'] = dueout
                
    sql = "SELECT  sum(adult) +  sum(child1) + sum(child2)  "\
        "    FROM reservation "\
         "  WHERE STATUS = 100 AND  property = '"  + property + "';"
     
    cur.execute(sql)
    arrivals = cur.fetchone()[0]
               
    qresults['arrivals'] = arrivals
    
            
    sql = "SELECT  count(*)  "\
        "    FROM roomtype_rooms "\
         "  WHERE active = 1 AND hskpclean = 0 AND   property = '"  + property + "';"
     
    cur.execute(sql)
    hskdirty = cur.fetchone()[0]
    
    qresults['hskdirty'] = hskdirty
    
    sql = "SELECT  count(*)  "\
        "    FROM roomtype_rooms "\
         "  WHERE active = 1 AND clean = 0 AND   property = '"  + property + "';"
     
    cur.execute(sql)
    hskdirtyocc = cur.fetchone()[0]
    qresults['hskdirtyocc'] = hskdirtyocc
    
    
    sql = "SELECT  count(*)  "\
        "    FROM roomtype_rooms "\
         "  WHERE active = 1 AND hskpclean = 1 AND   property = '"  + property + "';"
     
    cur.execute(sql)
    hskclean = cur.fetchone()[0]
    
    qresults['hskclean'] = hskclean
    
    sql =     "SELECT COUNT (*) "\
        "    FROM roomtype_rooms_ooo "\
         "  WHERE ooo_date = '2012-10-12' AND ooi = 1  and property = '"  + property + "';"
     
    cur.execute(sql)
    outorder_ooi = cur.fetchone()[0]
    
    qresults['outorder_ooi'] = outorder_ooi
    
    sql =     "SELECT COUNT (*) "\
        "    FROM roomtype_rooms_ooo rtr "\
         "  WHERE ooo_date = '2012-10-12' AND ooi = 1  and property = '"  + property + "'"\
         "   AND NOT EXISTS ( "\
    "     SELECT rtrooo.ooo_date "\
               "       FROM roomtype_rooms_ooo rtrooo "\
               "      WHERE rtrooo.property = '"  + property + "' "\
                    "   AND rtrooo.ooo_date = '2012-10-12' "\
                    "   AND rtrooo.room = rtr.room "\
                        " AND rtrooo.ooi = 1); "\
     
    cur.execute(sql)
    outorder_ooo = cur.fetchone()[0]
    
    qresults['outorder_ooo'] = outorder_ooo
    
    sql =     "SELECT sum(rd.rate) "\
        "    FROM reservation_dates rd, reservation  "\
         "  WHERE reservation_date = '2012-10-12'  and reservation.property = '"  + property + "'"\
         " and rd.property = reservation.property"\
         " and rd.inventory = 1 "\
        "    AND (reservation.status = 100 OR reservation.status = 101);    " 
    cur.execute(sql)

    qresults['ratesum'] =  cur.fetchone()[0]
     
    qresults['occupypct'] = "{:3.2f}%".format( 100* ( qresults['totalrooms']/qresults['arrivals']))
    
    qresults['today'] = datetime.now().strftime("%A, %B, %d, %Y")
    
    return qresults
        
    