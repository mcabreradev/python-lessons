def getMayor(sueldos):
  return str(max(sueldos))

def getMenor(sueldos):
  return str(min(sueldos))

def getSumatoria(sueldos):
  return str(sum(sueldos))

def getPromedio(sueldos):
  return str( float( int(getSumatoria(sueldos)) / len(sueldos) ) )

def getGanancias(sueldos, tope = 50000):
  ganancias = 0

  for sueldo in sueldos:
    if (sueldo > tope):
      ganancias+=  sueldo * 0.14

  return str(ganancias)