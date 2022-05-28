import requests

print("Currency converter (USD/BRL - EUR/BRL):\n")

def conferValue(val):
  if(val is None):
    return "Value unavailable!"
  else:
    return "BRL " + str(round(val, 2))

r = requests.get('https://api.hgbrasil.com/finance')

if(r.status_code == 200):
  print('- USD value (sell): '+conferValue(r.json()['results']['currencies']['USD']['sell']))
  print('- USD value (buy): '+conferValue(r.json()['results']['currencies']['USD']['buy'])+'\n')
  print('- EUR value (sell): '+conferValue(r.json()['results']['currencies']['EUR']['sell']))
  print('- EUR value (buy): '+conferValue(r.json()['results']['currencies']['EUR']['buy']))
else:
  print('Request Error - "api.hgbrasil.com"')

