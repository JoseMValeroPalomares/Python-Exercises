import keyboard
import time
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Enviar mensaje")
        master.geometry("300x200")

        # Campo de entrada de texto
        self.entry = tk.Entry(master, width=30)
        self.entry.pack(pady=10)

        # Botón para iniciar envío de mensajes
        self.start_button = tk.Button(master, text="Iniciar envío de mensajes", command=self.iniciar_envio)
        self.start_button.pack(pady=10)

        # Botón para detener envío de mensajes
        self.stop_button = tk.Button(master, text="Detener envío de mensajes", command=self.detener_envio)
        self.stop_button.pack(pady=10)

        self.envio_activo = False

    def iniciar_envio(self):
        mensaje = self.entry.get()
        if mensaje != "" and not self.envio_activo:
            self.envio_activo = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            enviar_mensaje(mensaje)

    def detener_envio(self):
        self.envio_activo = False

    def cerrar_ventana(self):
        keyboard.unhook_all()
        self.master.destroy()

def enviar_mensaje(mensaje):
    while True:
        keyboard.write(mensaje)
        time.sleep(0.1)
        if not app.envio_activo:
            break

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_ventana)
    root.mainloop()