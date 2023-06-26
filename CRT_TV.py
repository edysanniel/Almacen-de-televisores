from TV import TV


class CRT_TV(TV):
    def __init__(self, serial, price, max_channels, pago):
        super().__init__(serial, price, max_channels, pago)

    def __eq__(self, other):
        return isinstance(other, CRT_TV) and super().__eq__(other)

    def getTipo(self):
        return "CRT"

    def consumo(self):
        return 50

    def print(self):
        print("Tipo:", self.getTipo())
        print("Serial: ", self.serial)
        print("Price: ", self.price)
        print("Max Channels: ", self.max_channels)
        print("Forma de Pago: ", self.pago)
