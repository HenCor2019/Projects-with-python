# Hello World program in Python
    
import pandas as pd #ocupada para generar tablas
import numpy as np #auxiliar para funciones
#TODO DE LA LIBRERIA SYMPY PARA EL CALCULO
from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S
from sympy import Derivative, diff, simplify
            ################
            #   FUNCIONES  #
            ################

#una funcion cualquiera
def f(x) :
    return np.sqrt(x+2)

#asignando los valores de x
x= np.array([-2,2,7])

#imprimiendo de forma vulgar
y=f(x)
#print(y)

#imprimiendo en formato tabla
table = pd.DataFrame( list ( zip (x,y)) , columns=('x','f(x)'))
#print(table)

printing.init_printing(use_latex='mathjax')
t = Symbol('t') # Creando el simbolo x.


            ##############
            #   LIMITES  #
            ##############
            
            
#definiendo una funcion
def f(t) :
    return np.power(t**2-t+2,1)

#asignando esa variable
z=f(t)
#Limit(z, t, 2).doit() forma de calcular el limite 
#z: la funcion , t : la variable , 2: donde se quiere evaluar
#print("el limite de tu funcion es: " + str(Limit(z, t, 2).doit()))


            ################
            #   DERIVADAS  #
            ################
            
# simplify(Derivative(z,t).doit()
#simplify : simplifica la expresion
#z: la funcion que quiero derivar
#t: la variable respecto a la cual derivo
#existe un tercer argumento para el orden de derivacion 
#simplify(Derivative(z,t,a).doit()

dt_dy= simplify(Derivative(z,t).doit())
#print(dt_dy)

#dt_dy= simplify(Derivative(z,t,2).doit())
#print(dt_dy)

#evaluar una derivada
print("la funcion evaluada en 1 es :" + str(diff(dt_dy, t).subs(t,1)))