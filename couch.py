import couchdb
import datetime


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
    print("  ID = {}".format(db[o]['_id']))
    for k in db[o]:
      if not (k == '_id' or k == '_rev'):
        print("\t{} : {}".format(k,db[o][k]))

def viewAll(c):
  for o in c:
    print('***{}***'.format(o))
    if not (o == '_replicator' or o == '_users'):
      db = c[o]
      viewDB(db)

def now():
  now = datetime.datetime.now()
  return now

def getDocItems(dType):
  r = []
  if dType.lower() == 'venue':
    r = [
      'name',
      'address1',
      'address2',
      'city',
      'state',
      'hashtag',
      'website',
      'gps',
      ]
  elif dType.lower() == 'artist':
    r = [
      'name',
      'info',
      'website',
      'hashtag',
       ]
  elif dType.lower() == 'region':
    r = [
      'gps_n',
      'gps_s',
      'gps_e',
      'gps_w',
      ]
  elif dType.lower() == 'crawler':
    r = [
      'site',
      'taglist',
       ]
  elif dType.lower() == 'agegroup':
    r = [
      'name',
      'info',
       ]

  return r

def add(dType,name):
  keys = getDocItems(dType)
  dic = {'type' : dType}
  print('Adding {} type Doc: {}'.format(dType,name))
  for i in keys:
    if i == 'name':
     dic[i] = name 
    elif i == 'taglist':
      l = []
      t = raw_input("Type a search tag: ")
      while (t != ''):
        l.append(t)
        t = raw_input("Type a search tag: ")
      if len(l) > 0: dic[i] = l
    else:
      t = raw_input("Type {} {}: ".format(dType,i))
      if t != '': dic[i] = t
  print('Adding {}'.format(name))
  return(dic)

def searchDB(db,dType,search):
  keys = getDocItems(dType)
  r = []
  for o in db:
    x = ''
    try:
      x = db[o]['name']  
    except:
      pass
    if x != '':
      if (search.lower() in x.lower()) or (x.lower() in search.lower()):
        #print('Found {} in {}'.format(search,x))
        r.append(db[o]['_id'])
  return r
