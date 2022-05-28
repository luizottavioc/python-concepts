import requests

def numberFormatting (n) :
  nStr = str(n)
  nNumb = len(nStr)
  formatted = ''

  if(nNumb > 6):
    slcN = slice(-6)
    if(str(nStr[slcN]) == '1'): 
      formatted = "Approx. "+str(nStr[slcN])+" million"
    else:
      formatted = "Approx. "+str(nStr[slcN])+" millions"

  elif(nNumb > 3):
    slcN = slice(-3)
    formatted = "Approx. "+str(nStr[slcN])+" thousand"

  else:
    formatted = "Exactly "+str(n)

  return formatted


r = requests.get('https://disease.sh/v3/covid-19/countries/Brazil')

if(r.status_code == 200):
  print('- Number of Covid-19 cases in Brazil all time: ' + numberFormatting(r.json()['cases']))
  print('- Number of Covid-19 cases in Brazil today: ' + numberFormatting(r.json()['todayCases']))
  print('- Number of Covid-19 deaths in Brazil all time: ' + numberFormatting(r.json()['deaths']))
  print('- Number of Covid-19 deaths in Brazil today: ' + numberFormatting(r.json()['todayDeaths']))
  print('- Number of active Covid-19 in Brazil: ' + numberFormatting(r.json()['active']))




