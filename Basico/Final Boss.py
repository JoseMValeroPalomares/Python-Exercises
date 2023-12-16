print("\n","Estas en tu habitacion ")
hacer=input("Quieres quedarte o salir")
if hacer == "quedarte":
    print("Has escuchado algo")
    hacer=input("Quedarte o salir")
    if hacer =="Quedarte":
        print("un asesino entro y te asesino")
    elif hacer=="salir":
        print("Te encuentras con un asesino y te asesina ")
elif hacer == "salir":
    hacer = input("A donde vas ahora: cocina,salon,cuarto")
    if hacer == "cocina":
        hacer = input("Quieres comer algo?")
        if hacer =="Si":
            hacer=input("Que quieres comer: Platano, Chorizo, Atun")
            if hacer=="Platano":
                print("Te comes el platano, pero estaba envenenado y mueres ")
                exit()
            elif hacer=="Chorizo":
                print("Te comes el platano, pero estaba envenenado y mueres ")
                exit()
            elif hacer=="Atun":
                print("Te comes un atun")
                hacer=input("Que haces ahora Salir o Quedarte")
                if hacer=="Salir":
                    print("Un asesino entro a tu casa pero no habia nadie")
                elif hacer=="Quedarte":
                    print("Un asesino entro a tu casa y te asesino")
        elif hacer =="No":
            hacer = input("Que haces ahora Salir o Quedarte")
            if hacer == "Salir":
                print("Un asesino entro a tu casa pero no habia nadie")
            elif hacer == "Quedarte":
                print("Un asesino entro a tu casa y te asesino")
    elif hacer == "salon":
        hacer =input("Que haces ahora: tele o salir(casa)")
        if hacer=="tele":
            print("Un asesino entro a tu casa y te asesino")
        elif hacer=="salir":
            print("Un asesino entro a tu casa pero no habia nadie")

    elif hacer == "cuarto":
        print("Un asesino entro a tu casa y te asesino")



