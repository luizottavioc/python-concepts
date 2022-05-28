import random

vet = []
corresp = []

for i in range(100):
  vet.append(random.randint(0,100))
print("Your array has already been incremented with 100 random numbers!")

n = int(input("Now, enter the integer number you want to find in array:"))
for i in range(len(vet)):
  if(vet[i] == n):
    corresp.append(i)

qtCorresp = vet.count(n)

print("------------------")
print("Array:\n"+str(vet))
print("------------------")
print("Count of times your number was found: "+str(qtCorresp))
print("Positions where the number was found: "+ str(corresp))
