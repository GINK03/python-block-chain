
import json

#while True:

cor = '00ce7c3a81315250d7abc2d99f177b2ffb442334644044ea89f1d6e435845d86'

while True:
  obj = json.load( open(f'cache/{cor}') )
  prev_hash = obj['prev_hash']
  data = obj['data']
  print( data )

  if data == 'Ground Zero':
    break
  cor =  prev_hash
