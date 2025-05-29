import tkinter as tk
ventana = tk.Tk()

boton = tk.Button(ventana, text="Enviar", command=lambda: print("Hola"), font=("Arial", 14))
boton.pack(pady=10)  # Añadir un espacio vertical


ventana.mainloop()