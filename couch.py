import couchdb
from uuid import uuid4


def connectSRV(srv = 'http://localhost:5984'):
  c = couchdb.Server(srv)
  return c
  
def createDB(c,name):
  if name not in c:
    #doc_id = uuid4().hex
    db = c.create(name)
  else:
    db = connectDB(c,name)
  return db  
    
def connectDB(c,name):
  db = c[name]
  return db

def save(db,dic):
  db.save(dic)

def view(db,s):
  for o in db:
    x='N/A'
    try:
      x = db[o][s]  
    except:
      pass
    print(x)

def viewDB(db):
  for o in db:
    #print("\tID = {} -- {}".format(db[o]['_id'],db[o]['_rev']))
    for k in db[o]:
      if not (k == '_id' or k == '_rev'):
        print("\t{} : {}".format(k,db[o][k]))

def viewAll(c):
  for o in c:
    print('***{}***'.format(o))
    if not (o == '_replicator' or o == '_users'):
      db = c[o]
      viewDB(db)

