'''
metodo de biseccion
formula ocupada :
 lower_limit + (upper_limit - lower_limit)/2

se cambia el intervalo que tenga el mismo signo que la nueva iteracion

f(upper_limit) y f(lower_limit) deben de ser estrictamente diferentes , eso garantiza el corte

'''


#funcion de ejemplo
function = "x**2 + 4*x-10"

#intervalo
u_limit = 2
l_limit = 1

new_valor = 0.0


#define que haya un corte
def exits(u,l) :
 if eval_intervals(u) * eval_intervals(l) < 0 :
  return True
 return False

#evalua los intervalos
def eval_intervals(x) :
 return eval(function)
 
if exits(u_limit , l_limit ) :
 for i in range(30) :
   new_valor = l_limit + (u_limit - l_limit )/2
   
   if eval_intervals(new_valor) * eval_intervals(l_limit ) < 0 :
     u_limit = new_valor 
   else :
     l_limit = new_valor
     
 print("raiz : " + str(round(new_valor, 4)))
else :
 print ("no hay cortes en ese intervalo...")
