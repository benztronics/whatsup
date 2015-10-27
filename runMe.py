# This will just use couch.py to connect and list all of the items in the local couchdb

import sys
import couch

if len(sys.argv) > 1:
  srv = sys.argv[1].lower()
else:
  srv = 'http://localhost:5984'

c = couch.connectSRV(srv)
couch.viewAll(c)

