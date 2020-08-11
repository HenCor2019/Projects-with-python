'''eriificando la creacion de un correo gmail
REGLAS : 
-Maximo de 30 caracteres
-Solo se permiten caracteres de tipo alfanumerico y opcionalmente un '.'
-Debe terminar con '.com'
'''

import re

pattern = re.compile(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{1,6}\b")
flag = True

mails = """raul.lopez@relopezbriega.com, Raul Lopez Briega,
foo bar, relopezbriega@relopezbriega.com.ar, raul@github.io, 
https://relopezbriega.com.ar, https://relopezbriega.github.io, 
python@python, river@riverplate.com.ar, pythonAR@python.pythonAR
"""
print(mails)
print(pattern.findall(mails))

'''
while flag :
 Gmail = input("Correo : ")
 if pattern.search(Gmail) is not None :
    flag = False
    print("correo exitoso")
 else :
     print("revisa tu correo de nuevo")
'''
#example_list= [0,1,2,3,4,5]
#print(example_list[:3]) # muestra los primeros 3

