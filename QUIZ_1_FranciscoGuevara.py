#QUIZ 1 PROGRAMACION
#Francisco Guevara C.I 26604913 


var_n =  int(input("Ingrese la cantidad de terminos: "))


lista1 = []  #Lista de numeros semiprimos
lista = []   #lista de numeros Fibonacci


for i in range(1,var_n+1):


	if i == 1:
		lista.append(1)  #ingresando los primeros 2 terminos de los numero de Fibonacci y los numeros semiprimos
		lista1.append(1)


	elif i == 2:
		lista.append(2)
		lista1.append(2)


	else:
		contador = 0	  #algoritmo para generar N numeros semi primos	
		while len(lista1) < i:
			if (lista1[i-2] + 1+contador) % 2 == 0: # si el numero es par debe pasar por este algoritmo para verificar si es un numero es semiprimo
				count = 0
				for j in range(1,lista1[i-2]+1+contador):
					if (lista1[i-2]+1+contador) % j == 0:  # Buscando los divisores del numero 
						if j != 2 and j != lista1[i-2]+1+contador and j!=1 and j%2==0: # si alguno de los divisores del numero  es par ya no sera un numero semiprimo, y se sumara al contador
							count = count + 1
				if count == 0:  # si el contador es cero quiere decir que no hay divisores pares por lo tanto el numero es un numero semiprimo
					lista1.append(lista1[i-2]+1+contador)	


			else: #agregando directamente los numeros impares a la lista1 de numeros semiprimos
				lista1.append(lista1[i-2]+1+contador)	
			contador += 1 


		ft = lista[i-2] + lista[i-3] #Generador de numero de Fibonacci
		lista.append(ft) 



suma = 0
for h in range(0,var_n):
	suma = suma + lista[h]/lista1[h]


print("\nLa suma de los primeros {} terminos es: {}".format(var_n,suma))



				

		
