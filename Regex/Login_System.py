#Sistema de login de gmail usando regex

import re 

def Options() :
    options = "1. Registrarse\n2. Ver usuarios\n3. Filtrar por deminio\n4. Salir\n"
    print(options)

    return  int(input("Elige una opcion : "))

def Domain_Verify(user) :
    if re.search(r"@gmail.",user) is not None and re.search(r"(@gmail.com)$",user) is not None :
        return True

    return False

def Verify(user,Mails) :
    for m in Mails : 
        if user == m : return True

    return False

def Register(Mails) :
    gmail_pattern = "(\w\.?){6,29}(@gmail.com)?"
    ilicit_words = "pene|vagina|pendejo|fuck|puto|puta"
    illegal_characters = "[\s#-=!\|/[]{}<>+)(*&^%$`@~';,]"

    tmp_user = input("usuario : ")
    tmp_password = input("contrase?a : ")

    if re.search(r"(\w\.?){6,29}@?",tmp_user) is not None and Domain_Verify(tmp_user) :

        if re.search(r"pene|vagina|pendejo|fuck|puto|puta",tmp_user) is not None or re.search(r"[\#\-\=\^\$\%\!]",tmp_user) :
           return "", ""

        if re.search(r"(@gmail.com)$",tmp_user) is None :
           return tmp_user+"@gmail.com", tmp_password
     
        if Verify(tmp_user,Mails) : return "",""
    
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
        username, password = Register(Mails)
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
