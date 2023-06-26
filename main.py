from TV_Storage import TV_Storage
from LED_TV import LED_TV
from CRT_TV import CRT_TV


if __name__ == "__main__":
    try:
        print("Creating and initializing...")
        storage = TV_Storage()

        print("Creating TVs...")
        tv1 = LED_TV("654662", 600, 30, "CREDIT", 45)
        tv2 = CRT_TV("826545", 520, 25, "CASH")
        tv3 = CRT_TV("464655", 340, 10, "CASH")
        tv4 = LED_TV("314158", 850, 100, "CREDIT", 56)
        tv5 = CRT_TV("314516", 700, 35, "CREDIT")

        print("Insertion testing...")
        storage.append(tv1)
        storage.append(tv2)
        storage.append(tv3)
        storage.append(tv4)
        storage.append(tv5)

        print("Printing list...")
        print("")
        storage.printData()

        print("================")
        print("")
        storage.printDetails()
        print("")

        print('Saving Data in "./data.txt"...')
        print("")
        storage.save("./data.txt")

        print("Run ended without any error... 😋")

    except Exception as e:
        print(f"An error ocurred: [{e}] 😥")
