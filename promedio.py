def calcular_promedio(numeros):
  suma = 0
  cantidad = len(numeros)

  if cantidad == 0:
    return 0

  for n in numeros:
    suma = n + suma

  total = suma / cantidad
  return total

print(calcular_promedio([2,3,4,5,6, 9]))