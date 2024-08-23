import numpy as np
#Generamos números aleatorios entre 1 y 9 con una estructura de 3X2
arr = np.random.randint(1,10,(3,2))
#imprimir la forma original del arreglo
print("Forma original:", arr.shape)
print(arr)
#Cambiamos la forma del arreglo a una forma de (1,6)
arr_reshaped = arr.reshape(1,6)
#Imprimimos la nueva forma
print("Arreglo después de reshape:", arr_reshaped.shape)
print(arr_reshaped)