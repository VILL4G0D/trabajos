# controlador.py
from modelo import CuentaBancaria
from vista import Vista

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutar(self):
        # Mientras la ventana esté abierta, seguimos mostrando la interfaz
        self.vista.root.mainloop()
    
    def realizar_deposito(self):
        cantidad = self.vista.pedir_cantidad("Depositar dinero")
        
        if cantidad <= 0:
            # Si la cantidad es menor o igual a cero, mostrar mensaje de error
            self.vista.mostrar_mensaje("La cantidad a depositar debe ser positiva.")
        else:
            saldo_actual = self.modelo.depositar(cantidad)
            self.vista.actualizar_saldo(saldo_actual)
            self.vista.mostrar_mensaje(f"Has depositado ${cantidad:.2f}. Nuevo saldo: ${saldo_actual:.2f}")
    
    def realizar_retiro(self):
        cantidad = self.vista.pedir_cantidad("Retirar dinero")
        if cantidad > 0:
            if self.modelo.retirar(cantidad):
                saldo_actual = self.modelo.consultar_saldo()
                self.vista.actualizar_saldo(saldo_actual)
                self.vista.mostrar_mensaje(f"Has retirado ${cantidad:.2f}. Nuevo saldo: ${saldo_actual:.2f}")
            else:
                self.vista.mostrar_mensaje("No tienes suficiente saldo para realizar esta operación.")
    
    def consultar_saldo(self):
        saldo = self.modelo.consultar_saldo()  # Obtiene el saldo desde el modelo
        self.vista.actualizar_saldo(saldo)  # Actualiza la vista con el saldo
        self.vista.mostrar_mensaje(f"Tu saldo actual es ${saldo:.2f}")  # Muestra el mensaje con el saldo
