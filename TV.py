class TV:
    def __init__(self, serial="INVALID", price=-1.0, max_channels=-1, pago="CASH"):
        self.serial = serial
        self.price = price
        self.max_channels = max_channels
        self.pago = pago

    def __eq__(self, other):
        return self.serial == other.serial and self.price == other.price and self.max_channels == other.max_channels and self.pago == other.pago

    def setSerial(self, new_serial):
        self.serial = new_serial

    def setPrice(self, new_price):
        self.price = new_price

    def setMaxChannels(self, new_max_channels):
        self.max_channels = new_max_channels

    def setFormaPago(self, new_pago):
        self.pago = new_pago

    def getSerial(self):
        return self.serial

    def getPrice(self):
        return self.price

    def getMaxChannels(self):
        return self.max_channels

    def getFormaPago(self):
        return self.pago

    def __str__(self):
        return f"Serial: {self.serial}\nPrecio: {self.price}\nMax Canales: {self.max_channels}\nForma de Pago: {self.pago}"

    def print(self):
        print("Serial: ", self.serial)
        print("Price: ", self.price)
        print("Max Channels: ", self.max_channels)
        print("Forma de Pago: ", self.pago)
