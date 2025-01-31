"""
           Autor:
   Juan Pablo Buitrago Rios
   juanybrisagames@gmail.com
   Version 2.0 : 31/01/2025 00:10am

"""
import numpy as np  #Importe para realizar calculos numérico
import matplotlib.pyplot as plt #Importe para realizar y visualizar gráficos

#Inicializar variables
epsilon = 1.0 #Inicio de la variable Epsilon en 1
iteracion = 0 #Contador de iteraciones
N_Iteraciones= [] #Guarda las iteraciones
L_Epsilon = [] #Guarda los valores de epsilon

#Ciclo para encontrar la precisión de máquina
while 1.0 + epsilon != 1.0:
    epsilon /= 2 #Cada iteración dividimos epsilon entre 2
    iteracion = iteracion + 1 #Incremento del contador por cada iteración
    N_Iteraciones.append(iteracion) #Guardamos el valor de la iteración
    L_Epsilon.append(epsilon) #Guardamos el valor de epsilon
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}") #Muestra los valores actuales

#Gráfica
plt.figure() #Crea una figura 
plt.plot(N_Iteraciones, L_Epsilon, label='Precisión de máquina', marker='o') #Grafica el valor de epsilon sobre cada iteración
plt.xlabel('Iteracion') #Nombre del eje X
plt.ylabel('Epsilon') #Nombre del eje y
plt.title('Precisión de máquina') #Título de la grafica
plt.show() #Muestra la gráfica en pantalla

#Valor final de la precisión de máquina
epsilon *= 2 #Se multiplica el último valor de epsilon por 2
print(f"Precisión de máquina: {epsilon}") #Muestra Epsilon en su valor final.