#Comprobando una fecha en formato dd/mm/yy
#ejemplo : 05/11/2009

import re 

condition = "^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/(1[7-9]([0-9]{2,2})|20[01][0-9]|2020)"

pattern = re.compile(condition) #patron predefinida

date = input("ingrese una fecha : ")

#verifica que el formato sea el indicado
if pattern.search(date) is not None :
 print("Formato correcto")
else : 
 print("Formato incorrecto")
