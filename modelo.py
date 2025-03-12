#modelo.py
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0.0  # Inicializamos el saldo en 0
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return False
        else:
            self.saldo -= cantidad
            return True

    def consultar_saldo(self):
        return self.saldo
