import json

import datetime

dt_now = datetime.datetime.now()

Str_dt_now = str(dt_now)

#while True:

cor = 'in the value'

val = cor

while True:
  obj = json.load( open(f'cache/{cor}') )
  prev_hash = obj['prev_hash']
  data = obj['data']
  print( data )

  if data == 'Kenzi Hashimoto':
    value = "true"
    print ('Content-Type: text/html\n');
    print ('<!doctype html>'); 
    print ('<html>'); 
    print ('<head>'); 
    print ('<title>Certificate_of_QR_code_in_HTML</title>'); 
    print ('<meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />'); 
    print ('<meta http-equiv="Content-style-Type" content="text/css" />'); 
    print ('<meta http-equiv="Content-Script-Type" content="text/javascript" />'); 
    print ('<meta name="author" content="GYOKUWADO" />'); 
    print ('<meta name="copyright" content="" />'); 
    print ('<meta name="description" content="QR_CODE_IN_THE_HTML_TO_SITE_OF_KUMO" />'); 
    print ('<meta name="keywords" content="KUMO" />'); 
    print ('<meta name="date" content="2022-01-13">'); 
    print ('<meta name="generater" content="notepad" />'); 
    print ('<meta name="robots" content="noindex">'); 
    print ('</head>'); 
    print ('<body>'); 
    print ('<table border="1">');
    print ('  <tr>');
    print ('    <td>Certificate Authority</td><td>KUMO</td>');
    print ('  </tr>');
    print ('  <tr>');
    print ('    <td>File Name</td><td>QR_IN_WWW.html</td>');
    print ('  </tr>');
    print ('  <tr>');
    print ('    <td>cor</td><td>' + val + '</td>');
    print ('  </tr>');
    print ('  <tr>');
    print ('    <td>Date</td><td>' + Str_dt_now + '</td>');
    print ('  </tr>');
    print ('  <tr>');
    print ('    <td>value</td><td>' + value + '</td>');
    print ('  </tr>');
    print ('</table>');
    print ('</body>'); 
    print ('</html>'); 
    break
  cor =  prev_hash
