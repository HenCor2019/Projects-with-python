# Propuesta parcial01
#Compras en un supermercado

list_product=[]
list_price=[]

#Funcion que se encarga de añadir productos
def buy() :
    product= ["papas","Queso","Papel higienico"]
    price = [0.50,0.60,2.50]
    
    op=int(input("\n1.Papas\n2.Queso\n3.Papel higienico\n opcion: "))
    if op > len(product) :
        print("producto invalido")
    elif product[op-1] in list_product :
       print("Ya posees ese producto")
    elif not product[op-1] in list_product :
        list_product.append(product[op-1])
        list_price.append(price[op-1])
        print("Agregado con exito")
    else :
        print("Producto invalido!")
 
#Borra algun producto       
def delete_product() :
        product= ["papas","Queso","Papel higienico"]
        price = [0.50,0.60,2.50]
        op=int(input("\n1.Papas\n2.Queso\n3.Papel higienico\n opcion: "))
        if op > len(product):
            print("Producto invalido!")
        else :
            list_product.remove(product[op-1])
            print("Eliminado con exito")

#menu principal
while True :
    op=int(input("\n1.Comprar\n2.Ver productos\n3.Borrar producto\n4.Total\n5.Salir\nOpcion: "))
    #opcion de compra
    if op== 1 :
        buy()
    #opcion de ver productos    
    elif op == 2 :
        i=0
        if len(list_product) == 0 :
            print("No hay productos actualmente")
        else :    
            while i < len(list_product) :
               print("producto: " + str(list_product[i]) +  " y su precio es: " + str(list_price[i]))
               i+=1
    #opcion de borrar productos
    elif op == 3 :
        if len(list_product) == 0 :
            print("No hay productos actualmente")
        else :
            delete_product()
    #Calcular el precio total
    elif op == 4 :
        if len(list_product) == 0 :
            print("No hay productos actualmente")
        else :
            total=0
            for p in list_price :
               total+=p
            print("Total a cancelar: $" + str(total))
    #Irse al carajo
    elif op == 5 :
        break;
    else :
        print("opcion erronea")
    
    
    