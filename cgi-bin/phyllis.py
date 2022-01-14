import json

import datetime

dt_now = datetime.datetime.now()

Str_dt_now = str(dt_now)

seed = 'S/N 0000'

#while True:

cor = '04b1004d758f1f04aca131956d6be10bbc76cafb84073c5a9702222904e77f26'

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
