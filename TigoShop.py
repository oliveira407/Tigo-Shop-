
print("======== TIENDA TIGO =========") 
print("1.- Recarga de credito")
print("2.- Doble carga")
print("3.- Paquetigos")
print("4.- Consulta")
print("=============================") 
select = int(input("Ingrese su opcion ")) 


if(select == 1):
    opcion = int(input("Ingrese su monto de recarga de credito "))
    print("Su monto de credito es " + str(opcion))
    print("Recarga exitosa")
    
    
elif(select == 2):     
    print("FELICIDADES Eligio su doble carga")
    print("1.- Si")
    print("2.- No")
    doble = int(input("Ingrese su opcion "))
    if(doble == 1):
        print("Se activo la doble carga")
    elif(doble == 2):
        print("Doble carga cancelado")    

elif(select == 3):    
   print("Paquetigos Disponible")
   print("1.- Internet Ilimitado por 24hrs -> 10 Bs ")
   print("2.- 500 Mb  -> 5 bs ")
   print("3.- 5 mn -> 3 Bs ")
   paquetigos = int(input("Ingrese su Opcion "))
   if(paquetigos == 1):
       print("Usted tiene Internt Ilimitado por 24 hrs")
   elif(paquetigos == 2):
       print("Usted tiene 500 Mb ")
   elif(paquetigos == 3):
       print("Tiene 5 minutos de Llamada ")  

elif(select == 4):    
    print("Su saldo de Credito es ")
    print("Su saldo en Paquetigos es ")
    print("Le queda mn ")
print("=============================")








###  3- paquetigos 
            ###1. 350 Mb por 3.00 
            ###2. Interner ilimutado 10 bs
            ###3. 4 mn por 5 b         
###  4- consulta
###     muestra el saldo  "Su saldo disponible es" "
###     saldo de paquetigos es 
###     saldo de lla
