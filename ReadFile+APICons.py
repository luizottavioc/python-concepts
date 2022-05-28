import requests

file = open('/content/ceps.txt').read()

# content of file:
# 30535370 30692000 31080440 31550490 31990020 30411030

ceps = file.split(' ')
for cep in ceps:
  print("- Request CEP: "+str(cep))
  r = requests.get('https://viacep.com.br/ws/'+str(cep)+'/json/')
  if(r.status_code == 200):
    print("- Street name: "+str(r.json()['logradouro']))
    print("---------------------------")
  else:
    print('error - request!')
