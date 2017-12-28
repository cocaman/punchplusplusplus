#!/usr/bin/env python

import urllib2
import argparse
from keys import APIKEY

URL = 'https://punchplusplusplus.miscreantpunchers.net/'

if not APIKEY:
    print "Missing APIKEY in keys, cancelling."
    quit()

parser = argparse.ArgumentParser(description='Interact with the Punch++ REST API (read only mode)')
parser.add_argument('endpoint', metavar='endpoint', type=str, help='endpoint to hit', choices=['analytics', 'results', 'notes', 'users'])
parser.add_argument('-i, --id', dest='id', help='query for a single id for an action', type=int, metavar="ID")

args = parser.parse_args()

try:
    if args.id:
        req = urllib2.Request(URL + args.endpoint + '/' + str(args.id))
    else:
        req = urllib2.Request(URL + args.endpoint)
    
    req.add_header('apikey', APIKEY)
    req.add_header('Accept', 'application/json')
    req.add_header('Content-Type', 'application/json')
    resp = urllib2.urlopen(req)
    service_json = resp.read()

    print service_json

except urllib2.HTTPError, e:
    print "Nothing found puncher. Status code was " + str(e.code)
