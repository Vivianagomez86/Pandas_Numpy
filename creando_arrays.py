import numpy as np

#lista = list (range(0,10)) #start 0 10stop no se incluye
lista = np.arange(0,10)
lista = np.arange(0,20)
lista = np.arange(0,20,2) #step de 2 en 2
lista = np.zeros(3) #array de 3 ceros
lista = np.zeros((10,10)) #array de 10x10 de ceros
lista = np.ones ((10,5)) #array de 10x5 de unos
lista = np.linspace(0,10,10)
lista = np.linspace(0,10,100)
lista = np.eye(4)
lista = np.random.rand()
lista = np.random.rand(4)
lista = np.random.rand(4,5)
lista = np.random.randint(1,15)
lista = np.random.randint(1,100,(10,10))
print(lista)