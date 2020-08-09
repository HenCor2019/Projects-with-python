#Sistema de login usando regex

import re 

#opciones de usuario
def Options() :
 options = "1. Registrarse\n2. Ver usuarios\n3. Filtrar por deminio\n4. Salir\n"
 print(options)
 return  int(input("Elige una opcion : "))

def Register() :
 #valido para correos 'gmail'
 gmail_pattern = "(\w\.?){6,29}(@gmail.com)?"
 ilicit_words = "pene|vagina|pendejo|fuck|puto|puta"
 illegal_characters = "[\s#-=!\|/[]{}<>+)(*&^%$`@~';,]"

 tmp_user = input("usuario : ")
 tmp_password = input("contrase?a : ")

 if re.search(r"(\w\.?){6,29}",tmp_user) is not None :
     
     if re.search(r"pene|vagina|pendejo|fuck|puto|puta",tmp_user) is not None or re.search(r"[\#\-\=\^\$\%\!]",tmp_user) :
        return "", ""

     if re.search(r"(@gmail.com)$",tmp_user) is None :
         return tmp_user+"@gmail.com", tmp_password
     
     return tmp_user,tmp_password
 else :
     return "", ""

#variables
flag = True
username = ""
password = ""

Mails = {}

while flag :
 option = Options()
 if option == 1 :
     username, password = Register()
     if username == "" or password == "" :
         print("No se logro agregar el correo")
     else :
         Mails[username] = password
         print("Agregado con exito")
 elif option == 2 :
     print(Mails)
 else :
     flag= False
     print("Hasta la proxima")
