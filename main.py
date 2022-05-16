archivo = open('Paises_2.txt', 'r')

#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""

2 #Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""

3 #Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#4 
"""
4
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#5
"""
5
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""

#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in pais:
  if (i[0]=="U"):
    print(i)
for i in ciudad:
  if(i[0]=="U"):
    print(i)
    """
#Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  print(i)
print(len(paises))
"""
"""
#Busque e imprima la ciudad de Singapur
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print(c)
print(i)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="Venezuela"):
    print(i)
    print(ciudad[c-1])
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in pais:
  if (i[0]=="E"):
    print(ciudad)
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="Colombia"):
    print(ciudad[c-1])
"""
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
lista=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="México"):
    print(c)
"""
#Agregue un país que no esté en la lista 
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
pais.append("Wakanda")
pais.sort()
c=0
listac=[]
for i in pais:
  c+=1
  if(i=="Wakanda"):
    ciudad.insert(c-1,"Forever")
    print(pais[c-1],":",ciudad[c-1])
    print(c)