import tkinter as tk
ventana = tk.Tk()
def actua():
    print("Has pulsado el botón") 
boton = tk.Button(ventana, text="Enviar", command=actua, font=("Arial", 14))
boton.pack(pady=10)  # Añadir un espacio vertical

ventana.mainloop()