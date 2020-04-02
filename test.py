#!/usr/bin/env python
import requests
import random, time
url = 'http://localhost:5000'
authen = {'username': 'admin', 'password':'admin'}
unauthen = {'username': 'admin', 'password':'dasdasdn'}

endpoints = ["/", "/notfound", "/delay", "/home", "/calculator"]

while True:
  endpoint = random.choice(endpoints)
  if ( endpoint == "/"):
    passwords = ["admin","wrongpass"]
    password = random.choice(passwords)
    x = requests.post("%s%s" %(url, endpoint), data = {"username": "admin", "password": password})
  elif ( endpoint == "/calculator"):
    expressions = ["5+6","69-123","0/5","2*4+2"]
    expression = random.choice(expressions)
    x = requests.post("%s%s" %(url, endpoint), data = {"expression": expression})
  else:
    x = requests.get("%s%s" %(url, endpoint))
  print(x)
  time.sleep(3)