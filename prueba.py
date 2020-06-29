lista = [1, 2, 3, 5, 6, 7, 8]
pares = []
impares = []

for i in lista:
  if i % 2 == 0:
    pares.append(i)
  else:
    impares.append(i)

print("los pares " + str(pares))
print("los impares " + str(impares))