# Metodo falsa posicion
#Encuentra las raices por operaciones
#Ejemplo:
#funcion: x**2 - 4
#limite inferior : 0
#limite superior : 2

function= input("Escribe la funcion: ")

#limites de la funcion
lower_limit = float ( input ( "limite inferior: " ) )
upper_limit = float ( input ( "limite superior: " ) )

limit= 0.001 #limite del 0.1%


#Evalua en la funcion
def false_p(x) :
    return eval(function)

#verfica que el error sea menor al dado    
def finish(x) :
    if abs(eval(function)) < limit :
        return True
    return False
#realiza maximo 100 iteraciones
while range(100) :
 new_iteration =(lower_limit*(false_p(upper_limit)) - 
 upper_limit*(false_p(lower_limit)))/(false_p(upper_limit)-false_p(lower_limit))
 
#verifica la tolerancia
 if finish(new_iteration) :
     break;
#si no ha terminado,hace los cambios
 elif false_p(lower_limit)*false_p(upper_limit) > 0 :
       lower_limit = float(new_iteration)
 else :
    upper_limit = float(new_iteration)
    
     
print("valor de una raiz: "+ str(round(new_iteration,1)))