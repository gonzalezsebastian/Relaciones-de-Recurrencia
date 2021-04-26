def sin_repetidos(a,b):
  #Condición: Números enteros positivos entre a y b, inclusive, que no tienen dígitos repetidos.
  elementos = list(range(a, b+1))
  for numero in elementos:
    #Si el set del numero, tiene menor longitud que el mismo número, tiene digitos repetidos.
    if(len(set(str(numero))) < len(str(numero))):
      elementos.remove(numero)
  return (len(elementos), elementos)


def sin_ceros(a,b):
  #Condición: Números enteros positivos entre a y b, inclusive, que no tienen al 0 como dígito.
  elementos = list()
  for i in range(a, b+1):
    if not str(i).__contains__("0"):
      elementos.append(i)
  return (len(elementos), elementos)

def ascendentes(a,b):
  #Condición: Números enteros positivos entre a y b, inclusive, que tienen sus dígitos de manera estrictamente ascendente. Por ejemplo: 1468 cumple la condición, pero 14668 no la cumple.
  elementos = list()
  for i in range(a, b+1):
    if asciende(i):
      elementos.append(i)
  return (len(elementos), elementos)

def asciende(num):
  s = str(num)
  for i in range(len(s)-1):
    if int(s[i]) >= int(s[i+1]):
      return False
  return True


def conjuntos_sin_consecutivos(a,b,r)-> tuple:

  numbers = list(range(a,b+1))
  retList = list()
  n = len(numbers)
  #Cuando 2r < n no hay posibles, entonces retornamos la lista vacía
  if 2*r > n:
    return retList

  #Creamos una lista de indices para poder iterar las posibles combinaciones
  indices = list(range(r))

  while True:
    """
    Este for lo utilizamos para conocer si algun indice puede ser incrementado 
    Esto se hace recorriendo la lista de indices de derecha a izquierda y verificando que el indice no sea igual al valor maximo que puede alcanzar.
    Si hay alguno que pueda ser incrementado, entonces salimos del ciclo y continuamos
    Si recorre el ciclo y no encontró alguno que pueda ser incrementado entonces devolvemos la lista pues no hay otra combinacion posible, este es el else
    """
    for i in reversed(range(r)):
        if indices[i] != i + n - r:
            break
    else:
        return (len(retList), retList)

    #Aqui incrementamos el indice que encontramos que podía ser incrementado en el for anterior
    indices[i] += 1

    #Corregimos todos los indices que están a la derecha del que se incrementó
    for j in range(i+1, r):
        indices[j] = indices[j-1] + 1
    
    #Se crea una lista temporal con los valores en los que se encuentran los indices y se verifica si cumple con la condicion de que no tengan numeros consecutivos
    tempList = [numbers[i] for i in indices]
    for e in range(len(tempList)-1):
      if tempList[e] + 1 == tempList[e+1]:
        break
    else:
      #Si no posee números consecutivos se añade a la lista
      retList.append(tuple(tempList))

a = int(input("Ingrese el valor de a "))
b = int(input("Ingrese el valor de b "))
k = int(input("Ingrese el valor de k "))
print()

print("Sin repetidos: ",sin_repetidos(a,b))
print("Sin ceros: ",sin_ceros(a,b))
print("Digitos ascendentes: ",ascendentes(a,b))
print("Sin consecutivos: ",conjuntos_sin_consecutivos(a,b,k))