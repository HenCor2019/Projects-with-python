import random as rnd
import numpy as np

#variables
s_name = np.array([])
s_carnet = np.array([])
flag = True
op = 0

#opciones que puede hacer el usuario
def Options() :
 option = "1. Agregar\n2. Buscar\n3. Salir\n"
 print(option)
 op = int(input("opcion: "))
 return op

#retorna la tupla de valores de carnet y estudiante
def Create_Student(names,carnets) :
 name = input("nombre: ")
 names = np.append(names,name)
 carnet = "00"+ str(rnd.randint(1000,9999)) + "20"
 carnets = np.append(carnets,carnet)
 return names,carnets

#muestra los datos del estudiante
def Show_Student(s) :
 for student,carnet in zip(s_name,s_carnet) :
   if student == s :
     print("estudiante: " + str(student))
     print("carnet: " + str(carnet))

while flag :
 op = Options() 

 if op == 1 : #agregar estudiante
  s_name,s_carnet = Create_Student(s_name,s_carnet)
 elif op == 2 : # buscar estudiante
  tmp_student = input("estudiante: ")
  Show_Student(tmp_student)
 elif op == 3 : # salir del programa
  print("Hasta la proxima!!")
  flag = False 
 else :
  print("opcion erronea!!")
