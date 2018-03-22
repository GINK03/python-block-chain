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
  source_host, data = arg

  now = time.time()
  loc = datetime.fromtimestamp(now)
  timestamp = loc.timestamp()
  print(timestamp)
  
  block = { \
    'timestamp':timestamp, 
    'source_host':source_host,
    'data':data, \
  }
  print(block)
  return block
  
def _machines(arg):
  port = arg

  my_host = f'http://localshot:{port}'

  if isinstance(port, int):
    class Handler(http.server.SimpleHTTPRequestHandler):
      def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
     
      def do_GET(self):
        print("Client requested:", self.command, self.path )
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        self.wfile.write(bytes("Hello World !",'utf8'))
     
      buff = []
      def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        _data = self.rfile.read(content_length) 
        _data = json.loads( _data.decode() )
        print( _data )
        self._set_response()
        if _data['data'] == 'start':
          next_block = _gen_block((my_host, random.random()))
          kickback_host = _data['source_host']
          print('indata',kickback_host, next_block)
          #r = requests.post(f'{kickback_host}', data=json.dumps(next_block) )
        else:
          buff.append( _data )
          #if len(buff) == 10:
          print('buff', buff)
        self.wfile.write(bytes( json.dumps(None),'utf8'))
           
    httpd = socketserver.TCPServer(('0.0.0.0', port), Handler)
    print(f"load p2p node of blockchine, host={my_host}")
    httpd.serve_forever()
  else:
    # 最初のシードのブロードキャスト 
    print('init broadcast')
    time.sleep(1.0)
    for port in ports:
      print('init', port)
      r = requests.post(f'http://localhost:{port}/test', data=json.dumps(start_block) )


ports = [port for port in range(1200, 1210)]
print(ports)


start_block = _gen_block(('http://localhost:1200', "start"))

with concurrent.futures.ProcessPoolExecutor(max_workers=11) as exe:
  exe.map(_machines, ports + ["start"])
_machines(1200)
