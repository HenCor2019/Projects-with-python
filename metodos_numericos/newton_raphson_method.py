#metodo newton-ranphson

import numpy as np #auxiliar para funciones
#TODO DE LA LIBRERIA SYMPY PARA EL CALCULO
from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S
from sympy import Derivative, diff, simplify

#array
values= np.array([])
x= Symbol( 'x')

#funcion
def f(x) :
    return np.power(x**2 - 4,1)

#trying return and integer  
def eval_ordinary(x,value) :
  x = np.insert (x,0,value)
  h = f(x)
  valor = h[0]
  return valor

#trying to return and integer
def eval_derivative(value) :
  another_value = diff(f(x),x).subs(x,value)
  return another_value


new_valor = 0
new_valor = new_valor - eval_ordinary(values,1.0)/eval_derivative(2.0)
print ( "iteracion de prueba : " + str(round(new_valor,2)) )