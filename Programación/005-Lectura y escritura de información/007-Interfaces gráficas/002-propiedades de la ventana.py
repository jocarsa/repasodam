import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x300")  # Ancho x Alto
ventana.configure(bg="lightblue")  # Cambiar el color de fondo
ventana.resizable(False, False)  # No permitir redimensionar la ventana
ventana.mainloop()