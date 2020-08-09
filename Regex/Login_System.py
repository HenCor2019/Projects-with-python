#Sistema de login de gmail usando regex

import re 

#Opciones del usuario
def Options() :
    options = "1. Registrarse\n2. Ver usuarios\n3. Buscar correo\n4. Salir\n"
    print(options)

    return  int(input("Elige una opcion : "))

def Gmail_Domain(user) :
    if re.search(r"@gmail\.|gmail",user) is None and re.search(r"(@gmail\.com)$",user) is None :
        return True

    return False

#Verificando que el correo no se repita
def Repeated_Emails(user,Mails) :
    for m in Mails : 
        if user == m : return True

    return False

#Registra a los usuarios
def Register(Mails) :

    tmp_user = input("usuario : ")
    tmp_password = input("contrase?a : ")

    #No espacios y no caracteres de mas
    if re.search(r"\S\w{6,16}@?",tmp_user) is not None and Gmail_Domain(tmp_user) :
        
        #No malas palabras o simbolos
        if re.search(r"pene|vagina|pendejo|fuck|puto|puta",tmp_user) is not None or re.search(r"[\#\-\=\^\$\%\!]",tmp_user) :
           return "", ""
        #Acregando o no @gmail.com
        if re.search(r"(@gmail.com)$",tmp_user) is None :
           tmp_user+="@gmail.com"
     
        if Repeated_Emails(tmp_user,Mails) : return "",""
    
        return tmp_user,tmp_password

    else :
        return "", ""

#variables
flag = True
username = ""
password = ""
Mails = {}

while flag :
 try :
    option = Options()
    if option == 1 : # Registrar usuario
        username, password = Register(Mails)
        if username == "" or password == "" :
            print("No se logro agregar el correo")
        else :
            Mails[username] = password
            print("Agregado con exito")
    elif option == 2 : # Ver lista de usuarios
        print(Mails)
    elif option == 3 : # Filtrar algun usuario
        tmp_user= input("correo: ")
        for mail in Mails : 
            if mail == tmp_user : 
                print("Correo : " + mail + "\nContrase?a : " + Mails[mail])
    elif option == 4 : # Salir
        flag= False
        print("Hasta la proxima")
    else : #Opcion erronea
        print("Opcion erronea!")
 except :
      print("Solo se permiten numeros")
