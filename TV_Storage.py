import os
from LED_TV import LED_TV
from CRT_TV import CRT_TV


class TV_Storage:
    def __init__(self):
        self.data = []

    def getTotalCount(self):
        return len(self.data)

    def getData(self):
        return self.data

    def insert(self, index, item):
        self.data.insert(index, item)
        return self.data

    def prepend(self, item):
        self.data.insert(0, item)
        return self.data

    def append(self, item):
        self.data.append(item)
        return self.data

    def remove(self, index):
        self.data.pop(index)
        return self.data

    def clear(self):
        self.data = []

    def getConsumoTotal(self):
        total = 0

        for item in self.data:
            total += item.consumo()

        return total

    def printData(self):
        for item in self.data:
            item.print()
            print("")

    def printDetails(self):
        print(f"Cantidad TV LEDs: {self.getLEDsCount()}")
        print(f"Cantidad TV CRTs: {self.getCRTsCount()}")
        print(f"Cantidad Total: {self.getTotalCount()}")
        print(f"Consumo Total: {self.getConsumoTotal()}")

    def save(self, filename):
        with open(filename, 'w') as f:
            for i in self.data:
                f.write(str(i) + '\n\n')
        return os.path.isfile(filename)

    def getLEDsCount(self):
        led_count = 0

        for item in self.data:
            if isinstance(item, LED_TV):
                led_count += 1

        return led_count

    def getCRTsCount(self):
        crt_count = 0

        for item in self.data:
            if isinstance(item, CRT_TV):
                crt_count += 1

        return crt_count

    def searchSerial(self, serial):
        index = -1

        for item in self.data:
            index += 1
            if item.getSerial() == serial:
                return item, index
        return False
