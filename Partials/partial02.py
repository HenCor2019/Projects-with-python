import random as rnd
import numpy as np

def Options() :
 option = "1. Agregar\n2. Buscar\n.Salir\n"
 print(option)
 op = int(input("opcion: "))

def Create_Student() :
 name = input("nombre: ")
 s_name = np.append(s_name,name)
 carnet = "00"+ str(rnd.randint(1000,9999)) + "20"
 s_carnet = np.append(s_carnet,carnet)

#muestra los datos del estudiante
def Show_Student(s) :
 for student,carnet in zip(s_name,s_carnet) :
   if student == s :
     print("estudiante: " + str(student))
     print("carnet: " + str(carnet))

#variables
s_name = np.array([])
s_carnet = np.array([])

while True :
 if Options() == 1 :
  Create_Student()
 elif Options() == 2 :
  tmp_student = input("estudiante: ")
  Show_Student(tmp_student)
 elif Options() == 3 :
  print("Hasta la proxima!!")
  break
 else :
  print("opcion erronea!!")
