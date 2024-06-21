shop = True
ILIMITADO = 10
MEGAS = 5
LLAMADAS = 3
credito = 0;
acumulado = 0 
acumulado_minutos = 0 
while shop:
    
    print("======== TIENDA TIGO =========") 
    print("1.- Recarga de credito")
    print("2.- Doble carga")
    print("3.- Paquetigos")
    print("4.- Consulta")
    print("5.- Salir")
    print("=============================") 
    select = int(input("Ingrese su opcion ")) 

    if(select == 1):
        opcion = int(input("Ingrese su monto de recarga de credito "))
        print("Su monto de credito es " + str(opcion))
        credito = credito + opcion
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
            if (credito >= ILIMITADO): 
                credito = credito - ILIMITADO
                print("Usted tiene Internt Ilimitado por 24 hrs")
            else:
                print("Usted no tiene saldo suficiente")    
        elif(paquetigos == 2):
            if (credito >= MEGAS):
                acumulado = acumulado + 500 
                credito = credito - MEGAS
                print("Se compro 500 Mb ")
            else:
                print("Usted no tiene saldo suficiente")    
        elif(paquetigos == 3):
            if (credito >= LLAMADAS):
                acumulado_minutos = acumulado_minutos + 5 
                credito = credito - LLAMADAS
                print("Compro 5 minutos de Llamada ")  
            else:
                print("Usted no tiene saldo suficiente") 
    elif(select == 4):    
        print("Saldo disponible " + str(credito))
        print("Su saldo en Paquetigos es " + str(acumulado))
        print("Le queda mn " + str(acumulado_minutos))
        
    elif(select == 5):
        print("===== GRACIAS POR TU VISITA ====")
        shop =  False
        

