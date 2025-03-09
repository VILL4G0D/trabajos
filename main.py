# main.py
import tkinter as tk
from Modelo import CuentaBancaria
from Vista import Vista  # Aquí se cambia 'vista' por 'Vista' (nombre de la clase)
from Controlador import Controlador

# Programa Principal
def main():
    root = tk.Tk()
    
    modelo = CuentaBancaria()
    vista = Vista(root)  # Asegúrate de que Vista esté correctamente inicializada
    controlador = Controlador(modelo, vista)
    
    # Configurar las acciones de los botones
    vista.depositar_button.config(command=controlador.realizar_deposito)
    vista.retirar_button.config(command=controlador.realizar_retiro)
    vista.consultar_button.config(command=controlador.consultar_saldo)
    
    # Ejecutar la interfaz gráfica
    controlador.ejecutar()

# Ejecutamos el programa
if __name__ == "__main__":
    main()
