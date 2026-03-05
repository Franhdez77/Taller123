print ("Bienvenido al cajero")
contador=0
valorinicial=1000 

def inicio():
    operaciones=int(input("Cuantas operaciones va a realizar: "))
    if operaciones ==0:
        return inicio()
    else:
        return operaciones

def contraseña ():
    pin=(int(input("Ecribe la contraseña: ")))
    if pin==1234:
        return pin
    else:
        print("Contraseña incorrecta")
        return contraseña()
    
contraseña()

def retiro():
    retirar=float(input("Cuanto desea retirar: "))
    if retirar > valorinicial:
        print("Saldo insuficiente")
        return retiro()
    elif retirar <=0:
        print("Valor no disponible")
        return retiro()
    else:
        return retirar
    

def deposito():
    depositar=float(input("Cuanto desea depositar: "))
    if depositar > valorinicial:
        print("Saldo insuficiente")
        return retiro()
    elif depositar<=0:
        print("Valor no disponible")
        return retiro()
    else:
        return depositar
       



inicios=inicio()

while contador<inicios:
        
        print("1-Consultar saldo")
        print("2-Retirar dinero")
        print("3-Depositar dinero")
        print("4-Salir")
        menu=int(input("selecciona una opcion: "))
        
        if menu ==1:
            print ("su saldo es", valorinicial)
            contador+=1
        elif menu ==2:
             retirar=retiro()
             valorinicial -= retirar
             print("su nuevo saldo es ",valorinicial)
             contador+=1
        elif menu==3:
             depositar=deposito()
             valorinicial += depositar
             print("su nuevo saldo es: ",valorinicial)
        elif menu ==4:
            print("gracias por usar el cajero")
            break
        else: 
            print("Opcion no valida. Intente nuevamente")







    

