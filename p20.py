print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

def tri_recursion(k):
#Verifica si k es mayor que 0
  if(k > 0):
#Llama a la función de forma recursiva y suma el valor actual de k
    result = k + tri_recursion(k - 1)
#Imprime el resultado acumulado de la recursión
    print(result)
  else:
#Si k es 0, el resultado es 0
    result = 0
    # Retorna el resultado acumulado
  return result

#Mensaje que indica el inicio de los resultados de la recursión
print("\n\nRecursion Example Results")
#Llama a la función con el valor 6
tri_recursion(6)
