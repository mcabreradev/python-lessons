from sueldos import getMayor, getMenor, getSumatoria, getPromedio, getGanancias

sueldos = [30000, 45000, 234000, 56000, 34000, 78000, 100900, 65000, 37000, 43000, 124000, 76000, 25600]

print("La lista de sueldos: "+  str(sueldos))
print("El mayor sueldo es: "+ getMayor(sueldos))
print("El menor sueldo es: "+ getMenor(sueldos))
print("La sumatoria es: "+ getSumatoria(sueldos))
print("El promedio es: "+ getPromedio(sueldos))
print("El total de ganancias es: "+ getGanancias(sueldos))
