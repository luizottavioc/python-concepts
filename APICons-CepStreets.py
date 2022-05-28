import requests
import sys

state = input('Enter the state initials (Ex: MG, SP, RJ...): ').upper()

if(len(state) > 2):
  print("Apparently, you typed a wrong initial for the state, try again!")
  state = input('Enter the state initials (Ex: MG, SP, RJ...): ').upper()
  if(len(state) > 2):
    print("State initials are wrong!")
    sys.exit('Process closed')

city = input('Enter the city name: ')
rua = input('Enter the street name: ')

url = 'https://viacep.com.br/ws/'+state+'/'+city+'/'+rua+'/json/'
r = requests.get(url)

if(r.status_code == 200):
  if(len(r.json()) > 0):
    print('The corresponding CEP of your street request was: '+str(r.json()[0]['cep']))
  else:
    print('Your CEP request returned no results!')
else:
  print('Request Error! please confer the names entered!')