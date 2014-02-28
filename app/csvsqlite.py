'''
Created on Feb 28, 2014

@author: SG0166434
'''
import sqlite3
import MySQLdb
import re

global rowcount 
rowcount  = 0

def init(location):
    global conn
    global c
     
    conn = sqlite3.connect(location)
    c = conn.cursor()


def is_datetype(col):
    match = re.findall(r'(\d+-\d+-\d+)',col)
    print match,col
    if len(match) > 0:
        return True
    else:
        return False
    
def connect_mysql():
    db = MySQLdb.connect(host="10.14.149.47", # your host, usually localhost
                     user="valcar", # your username
                      passwd="valcar", # your password
                      db="valcar") # name of the data base
    global conn
    global c
    conn = db
    c = conn.cursor()

    
def load_csv(filename, tablename, delim=",", readone=False):
    rowcount = 0
    if readone:
        cfile = open(filename)
        header = cfile.readline().split(",")
        cfile2 = open(filename)
        cfile2.readline()
        first_row = cfile2.readline().strip().split(delim)
    else:
        content = open(filename).read()
        items = content.split("\n")
        header = items[0].split(delim)
        first_row = items[1].split(delim)
        
    cols = []
    for col in header:
        col = col[0:60].strip()
 #       print col
        cols.append(col.replace('"','').replace("(", "_").replace(" ", "_").replace(")","_").replace("#","_").replace("/",""))
    create_table(tablename, cols,c, first_row)
    
    if readone:
        while True:
            row = cfile.readline()
            if row == "":
                return
            row = read_row(row,delim,cols)
            insert_table(tablename, row,c,conn)
    else:
        for i in range(1, len(items)-1):
            row = read_row(items[i],delim,cols)
            insert_table(tablename, row,c,conn)
     
 
  
def get_coltype(colval):
    if is_datetype(colval):
        return "datetime"
    if colval.isdigit() and colval.find(".") != -1:
        return "decimal(10,3)"
    if colval.isdigit():
        return "int"
    return "varchar(255)"


def read_row(record, delim,cols):
        row={}
        colvals = record.split(delim)
        i=0
        for col in colvals:
            if len(col) > 0 and col[0] == '"':
                colvals[i] = col[1:len(col)-1]
                colvals[i] = colvals[i].replace('""', '"')
            i += 1
            
        i = 0
        for col in cols:
            #cleanup double quotes
            row[col] = colvals[i]
            i += 1
 #       print row
        return row
   
    
def insert_table(tabname, row, c,conn):
    global rowcount
    #get metadata to retrieve correct colorder
    c.execute("Select * from " + tabname + " where 1=2;")
    cols = [i[0] for i in c.description]
  #  cols = row.keys()
 #   print cols
    sql = 'insert into ' + tabname + ' values ('
    for col in cols:
        #cleanup for '
        row[col] = row[col].replace("'", "''")
        sql += "'" + row[col] + "',"
    sql = sql[0:len(sql)-1] 
    sql = sql + ");"
#    print sql
    try:
        c.execute(sql)
        rowcount += 1
        if (rowcount %1000 == 0):
            print "Table: %s, Rows:%d" % ( tabname, rowcount)
            conn.commit()
            c.execute("begin;")
    except Exception as e:
        print e
        print "=========================="
        print sql
    pass


def create_table(tabname, colnames,c, first_row):
    sql = 'drop table if exists ' + tabname + ";"
    print sql
    c.execute(sql)
    sql = "create table  " + tabname + " ("
    idx = 0
    for col in colnames:
        coltype = get_coltype(first_row[idx])
        sql += col + ' ' + coltype + " ," 
        idx += 1
    sql = sql[0:len(sql)-1] 
    sql = sql + ");"
    print sql
    c.execute(sql)
    pass
