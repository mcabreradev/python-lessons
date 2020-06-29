def evaluar(nom, ape):
  if  int(len(nom))<10 and int(len(ape))<10:
    print ("Nombre y apellido correctos")
  else:
    print("Nombre y/olargoooooo apellido muy largos")

nombre=""
apellido=""
nombre = str(input("Por favor introduzca nombre="))
apellido= str(input("Por favor introduzca apellido="))

evaluar(nombre,apellido)