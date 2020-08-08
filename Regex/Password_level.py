import re

password = input("costrase?a : ")


'''
debiles : solo menos de ocho alfanumericos 
ejemplo : 123abcde

intermedios : contras debiles que cuentan con al menos cuatro letras mayusculas
ejemplo : 123ABCDe

fuertes : contras intermedias;que cuentan con al menos dos simbolos
ejemplo : #123ABCDe=$
cant
'''

#variables 
ilicit_word = "pene|vagina|puto|pendejo"
ilicit_pattern = re.compile(ilicit_word)

simbols_password = False

alpha_numeric_password = False

capital_letter_password = False

password_level = "vulnerable"

quantity_simbols = len(re.findall("\W",password))

quantity_alpha_num = len(re.findall("\w",password))

quantity_capital_letter = len(re.findall("[A-Z]",password))

if re.search("\s",password) is None : 
 if ilicit_pattern.search(password) is None : 
  
  #caso debil
   if quantity_alpha_num >= 7 : 
   
       password_level = "debil"

  #caso intermedio
   if quantity_alpha_num >= 7 and quantity_capital_letter >= 4 :  

       password_level = "intermedia"
 
   #caso fuerte 
   if quantity_alpha_num >= 7 and quantity_capital_letter >= 4 and quantity_simbols >= 2 : 
 
       password_level = "fuerte"

 
   print("El nivel de tu contrase?a es : " + str(password_level))

 else :
   print("Algunas palabras no son admitidas")

else : 
 print("No puedes agregar espacios")

