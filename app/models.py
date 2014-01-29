'''
Created on Jan 28, 2014

@author: SG0166434
'''

from couchdb.mapping import (Document, IntegerField,ListField,FloatField, TextField, DictField, Mapping)
import couchdb

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
    
    
    
     
    
    