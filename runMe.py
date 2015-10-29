# This will just use couch.py to connect and list all of the items in the local couchdb
import sys
import couch

srv = 'http://localhost:5984'

def main():
  menu()

def viewAll():
  c = couch.connectSRV(srv)
  couch.viewAll(c)

def addEvent():
  c = couch.connectSRV(srv)
  db = c['event']
  item = raw_input("Search For Artist: ")
  f = couch.searchDB(db,'artist',item)
  count = 0
  menu = {}
  for a in f:
    count += 1
    menu[str(count)]=db[a]['name']
  options = menu.keys()
  options.sort()
  for entry in options:
    print entry, menu[entry]
  selection = raw_input("Please the Artist Number: ")
  print(menu[selection])

def addDoc(dType):
  c = couch.connectSRV(srv)
  db = c['event']
  if dType != 'crawler':
    item = raw_input("Type {} Name: ".format(dType))
    f = couch.searchDB(db,dType,item)
  else:
    f = []
    item = 'crawler'
  if len(f) < 1:
    dic = couch.add(dType, item)
    couch.save(db,dic)
  else:
    print('Found the Following Keys:')
    for a in f:
      print(a)


def menu():
  menu = {}
  menu['1']="View Database"
  menu['2']="View Whats Up"
  menu['3']="Add Something"
  menu['4']="Delete Something"
  menu['0']="Exit"
  while True:
    print('\n' * 50)
    now = couch.now()
    print("What's Up Tonight? - {}\n".format(now))
    options = menu.keys()
    options.sort()
    for entry in options:
      print entry, menu[entry]
    print('\n' * 5)
    selection = raw_input("Please Select a Number: ")
    if selection == '1':
      viewAll()
    elif selection == '2':
      print('Stream')
    elif selection == '3':
      addMenu()
    elif selection == '4':
      print('DeleteMenu')
    elif selection == '0':
      break
    else:
      print("{} : Please choose a number from list!".format(selection))
      continue
    xx = raw_input("Hit Enter to Continue...")

def addMenu():
  menu = {}
  menu['1']="Add a venue"
  menu['2']="Add an artist"
  menu['3']="Add a region"
  menu['4']="Add a crawler"
  menu['5']="Add an agegroup"
  menu['6']="Add an event"
  menu['0']="Exit"
  while True:
    print('\n' * 50)
    print("Add Menu\n")
    options = menu.keys()
    options.sort()
    for entry in options:
      print entry, menu[entry]
    print('\n' * 5)
    selection = raw_input("Please Select a Number: ")
    if selection == '1':
      addDoc('venue')
    elif selection == '2':
      addDoc('artist')
    elif selection == '3':
      addDoc('region')
    elif selection == '4':
      addDoc('crawler')
    elif selection == '5':
      addDoc('ageGroup')
    elif selection == '6':
      addEvent()
    elif selection == '0':
      break
    else:
      print("{} : Please choose a number from list!".format(selection))
      continue
    xx = raw_input("Hit Enter to Continue...")

if len(sys.argv) > 1:
  srv = sys.argv[1].lower()
main()
