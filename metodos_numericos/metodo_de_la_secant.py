'''
Metodo de la secante
formula :
 xi = xi-1 - ((xi-1 - xi-2)/(f(i-1)-f(i-2))) * f(i-1)

valores quemados porque no mo deja pedir desdo el telefono
'''
#ocupando la libreria para los array
import numpy as np

#ejemplo de funciones
function = "x**3 + 2*x**2 + 10*x - 20"

#condiciones iniciales
f_value = 0
s_value = 1

#variables
i = 2
values = np.array([0.0,1.0])
new_valor = 0
LIMIT = 0.001 # error del 0.1%

#funcion para evaluar
def eval_value(x) :
 return eval(function)

#terminar el ciclo
def finish (limit,vf,vo) :
 return (vf-vo) > limit
 

while finish(LIMIT, values[i-1],values[i-2]) or i < 20 :
 #formula
 new_valor = values[i-1] - ( (values[i-1] - values[i-2] ) / (eval_value(values[i-1]) - eval_value(values[i-2]) ) ) * eval_value(values [i-1])
 values = np.append(values,new_valor)
 i+=1

print("raiz : " + str(round(new_valor,4)))
