'''
Created on Mar 5, 2014

@author: SG0166434
'''
from couchdb.mapping import (Document, IntegerField,ListField,FloatField, TextField, DictField, Mapping)
import couchdb


class Other(Document):
    test = TextField()

class Customer(Document):
    
    name = TextField()
    addr = DictField(Mapping.build(
            city = TextField(),
            street = TextField()    
            ))
    other_ref = TextField()
    
    
    