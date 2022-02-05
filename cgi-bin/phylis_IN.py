import json

import datetime

dt_now = datetime.datetime.now()

Str_dt_now = str(dt_now)

seed = 'S/N 0001'

#while True:

cor = '02a6448aa805f17672d62a29e6dd46e7b1269618e296fca66d1215bca601385b'

val = cor

while True:
  obj = json.load( open(f'cache/{cor}') )
  prev_hash = obj['prev_hash']
  data = obj['data']
  print( data )

  if data == seed:
    print ('Content-Type: text/html\n');
    print ('true')
    print (val)
    print (Str_dt_now)
    break
  cor =  prev_hash
