import tkinter as tk
ventana = tk.Tk()
def actua():
    print("Has pulsado el botón") 
boton = tk.Button(ventana, text="Enviar",  font=("Arial", 14))
boton.pack(pady=10, padx=10)  # Añadir un espacio vertical y horizontal
boton.bind("<Button-2>", lambda event: actua())  # Asignar el evento de clic izquierdo del ratón
ventana.mainloop()