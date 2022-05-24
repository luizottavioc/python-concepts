fileTxt = open('/content/txt.txt', 'r')

# value of file:
# mouth//spent//revenue//responsible employee//value of biggest unqique spent//name of client
#
# april//2000//2300//Luiz//680//Gerdau
# may//1850//2000//Joao//570//Gerdau
# june//1900//2700//Gabriel//1050//Teksid

data = {
    'mouth': [],
    'spent': [],
    'revenue': [],
    'employee': [],
    'valBigstUnqSpent': [],
    'client': [],
}

insights = {
    'biggestSpent': [0, 0],
    'smallerSpent': [0, 0],
    'biggestProfit': [0, 0],
    'smallerProfit': [0, 0],
    'biggestSell': [0, 0],
}

i=0
for line in fileTxt:
  val = line.split('//')
  data['mouth'].append(val[0])
  data['spent'].append(float(val[1]))
  data['revenue'].append(float(val[2]))
  data['employee'].append(val[3])
  data['valBigstUnqSpent'].append(float(val[4]))
  data['client'].append(val[5])

  if(i == 0):
    insights['smallerSpent'][0] = i
    insights['smallerSpent'][1] = data['spent'][i]
    insights['smallerProfit'][0] = i
    insights['smallerProfit'][1] = data['revenue'][i] - data['spent'][i]

  if(data['spent'][i] > insights['biggestSpent'][1]):
    insights['biggestSpent'][0] = i
    insights['biggestSpent'][1] = data['spent'][i]

  if(data['spent'][i] < insights['smallerSpent'][1]):
    insights['smallerSpent'][0] = i
    insights['smallerSpent'][1] = data['spent'][i]

  if((data['revenue'][i] - data['spent'][i]) > insights['biggestProfit'][1]):
    insights['biggestProfit'][0] = i
    insights['biggestProfit'][1] = data['revenue'][i] - data['spent'][i]

  if((data['revenue'][i] - data['spent'][i]) < insights['smallerProfit'][1]):
    insights['smallerProfit'][0] = i
    insights['smallerProfit'][1] = data['revenue'][i] - data['spent'][i]

  if(data['valBigstUnqSpent'][i] > insights['biggestSell'][1]):
    insights['biggestSell'][0] = i
    insights['biggestSell'][1] = data['valBigstUnqSpent'][i]
  
  i+=1

print('----------------------')
print('Insights: ')
print('- Biggest Spent: '+str(insights['biggestSpent'][1])+' ('+str(data['mouth'][insights['biggestSpent'][0]] )+', '+str(data['employee'][insights['biggestSpent'][0]])+')')
print('- Smaller Spent: '+str(insights['smallerSpent'][1])+' ('+str(data['mouth'][insights['smallerSpent'][0]] )+', '+str(data['employee'][insights['smallerSpent'][0]])+')')
print('- Biggest Profit: '+str(insights['biggestProfit'][1])+' ('+str(data['mouth'][insights['biggestProfit'][0]])+', '+str(data['employee'][insights['biggestProfit'][0]])+')')
print('- Smaller Profit: '+str(insights['smallerProfit'][1])+' ('+str(data['mouth'][insights['smallerProfit'][0]])+', '+str(data['employee'][insights['smallerProfit'][0]])+')')
print('- Biggest Sell: '+str(insights['biggestSell'][1])+' ('+str(data['mouth'][insights['biggestSell'][0]] )+', '+str(data['employee'][insights['biggestSell'][0]])+')')

fileTxt.close()