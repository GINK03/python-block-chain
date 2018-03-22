import hashlib

import json

import http.server

import socketserver

import time

from datetime import datetime

import concurrent.futures

import requests

import random

def _gen_block(arg):
  source_host, data, prev_hash = arg

  now = time.time()
  loc = datetime.fromtimestamp(now)
  timestamp = loc.timestamp()
  print(timestamp)
 
  while True:
    nonce = random.randint(0, 100000000000000) 
    block = { \
      'timestamp':timestamp, \
      'source_host':source_host, \
      'data':data, \
      'prev_hash': prev_hash,  \
      'nonce':nonce,
    }
    next_hash = hashlib.sha256(bytes(json.dumps(block),'utf8')).hexdigest()

    # 先頭の4字が"0000"ならば、採用
    if next_hash[:4] == '0000':
      break
  open(f'cache/{next_hash}', 'w').write( json.dumps(block, indent=2, ensure_ascii=False) ) 
  print(next_hash)
  print(block)
  return block, next_hash

start_block, next_hash = _gen_block(('http://localhost:1200', 'Ground Zero', hashlib.sha256(bytes('0', 'utf8')).hexdigest()))
for line in open('stash/kokoro.txt'):
  line = line.strip()
  block, next_hash = _gen_block(('http://localhost:1200', line, next_hash) )


