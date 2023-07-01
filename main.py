# En un almacen se desea mantener un listado de los televisores que se almacenan en el mismo. 
# Un televisor tiene numero de serie,precio,cantidad de canales, la forma de pago y lo que consume 
# cada uno segun el tipo que sea led o crt.

from TV_Storage import TV_Storage
from LED_TV import LED_TV
from CRT_TV import CRT_TV


if __name__ == "__main__":
    try:
        print("Creating and initializing...")
        storage = TV_Storage()

        print("Creating TVs...")          # creando televisores
        tv1 = LED_TV("654662", 600, 30, "CREDIT", 45)
        tv2 = CRT_TV("826545", 520, 25, "CASH")
        tv3 = CRT_TV("464655", 340, 10, "CASH")
        tv4 = LED_TV("314158", 850, 100, "CREDIT", 56)
        tv5 = CRT_TV("314516", 700, 35, "CREDIT")

        print("Insertion testing...")     # agregando televisores
        storage.append(tv1)
        storage.append(tv2)
        storage.append(tv3)
        storage.append(tv4)
        storage.append(tv5)

        print("Printing list...")      # imprimiendo detalles de la lista
        print("")
        storage.printData()

        print("================")
        print("")
        storage.printDetails()
        print("")

        print('Saving Data in "./data.txt"...')   # guardando datos de lo tv
        print("")
        storage.save("./data.txt")

        print("Run ended without any error... 😋")  # capturando errores

    except Exception as e:
        print(f"An error ocurred: [{e}] 😥")
