# vista.py
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuenta Bancaria")
        
        # Solicitar el nombre del usuario
        self.nombre_usuario = simpledialog.askstring("Nombre de Usuario", "Por favor, ingresa tu nombre:")
        
        # Mostrar saludo en la interfaz
        self.saludo_label = tk.Label(root, text=f"Hola, {self.nombre_usuario}!")
        self.saludo_label.pack()
        
        self.saldo_label = tk.Label(root, text="Saldo: $0.00", font=("Arial", 14))
        self.saldo_label.pack(pady=10)
        
        self.depositar_button = tk.Button(root, text="Depositar dinero", font=("Arial", 12))
        self.depositar_button.pack(pady=5)
        
        self.retirar_button = tk.Button(root, text="Retirar dinero", font=("Arial", 12))
        self.retirar_button.pack(pady=5)
        
        self.consultar_button = tk.Button(root, text="Consultar saldo", font=("Arial", 12))
        self.consultar_button.pack(pady=5)
        
        self.salir_button = tk.Button(root, text="Salir", command=self.salir, font=("Arial", 12))
        self.salir_button.pack(pady=5)
    
    def actualizar_saldo(self, saldo):
        self.saldo_label.config(text=f"Saldo: ${saldo:.2f}")
    
    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)
    
    def pedir_cantidad(self, accion):
        cantidad = simpledialog.askfloat("Cantidad", f"Ingrese la cantidad para {accion}:")
        return cantidad if cantidad is not None else 0
    
    def salir(self):
        # Mostrar un mensaje de despedida antes de cerrar
        messagebox.showinfo("Despedida", f"Chao, {self.nombre_usuario}!")
        self.root.quit()  # Cierra la ventana

# Crear la ventana raíz (root) de la aplicación
root = tk.Tk()
vista = Vista(root)
root.mainloop()
