#metodo newton-ranphson
#valores quemados , porque desde el cel no puedo ingresar :'(

#todos los import 
import random as rnd
import numpy as np #auxiliar para funciones
from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S
from sympy import Derivative, diff, simplify

#valores de la variable definida
values= np.array([])
x= Symbol( 'x') #declara el simbolo

#funcion de prueba
def f(x) :
    return np.power(x-8,2)

#evalua en la original  
def eval_ordinary(x,value) :
  x = np.insert (x,0,value)
  h = f(x)
  valor = h[0]
  return valor

#evalua en la derivada
def eval_derivative(value) :
  another_value = diff(f(x),x).subs(x,value)
  return another_value

# declaracion de variables
LIMIT = 0.001

# intervalo
lower_limit = 0
upper_limit = 4

# valor entre el intervalo
new_valor = rnd.randint(lower_limit,upper_limit)

# saber si encontro la variable
find = False

#maximo 100 iteraciones
for i in range (100) :
 new_valor -=(eval_ordinary(values,new_valor) /
   											 eval_derivative(new_valor))
 if eval_ordinary(values,new_valor) < LIMIT :
  find = True
  break

#imprime dependiendo si la encontro
if find :
 print("raiz : " + str(round(new_valor,4)))
else :
 print("diverge... intenta de nuevo")

