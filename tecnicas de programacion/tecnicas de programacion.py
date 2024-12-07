from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


# Uso
circulo = Circulo(5)
print("Área del círculo:", circulo.calcular_area())

rectangulo = Rectangulo(4, 6)
print("Área del rectángulo:", rectangulo.calcular_area())
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Depósito realizado. Saldo actual: ${self.__saldo}")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro realizado. Saldo actual: ${self.__saldo}")
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return self.__saldo

# Uso
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)
cuenta.retirar(300)


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Vehículo {self.marca} modelo {self.modelo}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        return f"Automóvil {self.marca} modelo {self.modelo}, con {self.puertas} puertas"


# Uso
vehiculo = Vehiculo("Toyota", "Corolla")
automovil = Automovil("Honda", "Civic", 4)

print(vehiculo.describir())
print(automovil.describir())
class Ave:
    def hablar(self):
        print("Pío, pío")

class Loro(Ave):
    def hablar(self):
        print("Hola, soy un loro")

class Pato(Ave):
    def hablar(self):
        print("Cuac, cuac")

# Uso
aves = [Ave(), Loro(), Pato()]

for ave in aves:
    ave.hablar()
