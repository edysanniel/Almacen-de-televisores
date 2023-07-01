from TV import TV


class LED_TV(TV):
    def __init__(self, serial, price, max_channels, pago, cant_leds):
        super().__init__(serial, price, max_channels, pago)
        self.cant_leds = cant_leds

    def __eq__(self, other):
        return isinstance(other, LED_TV) and super().__eq__(other)

    def setCantLeds(self, new_cant_leds):
        self.cant_leds = new_cant_leds

    def getCantLeds(self):
        return self.cant_leds

    def getTipo(self):
        return "LED"

    def consumo(self):      # Consumo = 45 - 0.5*cant_leds
        return 45 - 0.5 * self.cant_leds

    def __str__(self):
        return f"Serial: {self.serial}\nPrecio: {self.price}\nMax Canales: {self.max_channels}\nForma de Pago: {self.pago}\nCantidad de LEDs: {self.cant_leds}"

    def print(self):
        print("Tipo:", self.getTipo())
        print("Serial: ", self.serial)
        print("Price: ", self.price)
        print("Max Channels: ", self.max_channels)
        print("Forma de Pago: ", self.pago)
        print("Cantidad de LEDs: ", self.cant_leds)
