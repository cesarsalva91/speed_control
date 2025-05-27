import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def iniciar_grafico(shared_data):
    def actualizar_reglas(event):
        ip = router_var.get()
        regla_box.set("")
        regla_box['values'] = []

        if ip in shared_data:
            opciones = [
                f"{regla_id} - {shared_data[ip][regla_id][-1]['comment'] or 'sin nombre'}"
                for regla_id in shared_data[ip]
            ]
            regla_box['values'] = opciones

    def actualizar_grafico(event=None):
        ip = router_var.get()
        regla_val = regla_var.get()

        if not ip or not regla_val or '-' not in regla_val:
            return

        regla_id = regla_val.split(" - ")[0]

        if ip not in shared_data or regla_id not in shared_data[ip]:
            return

        datos = shared_data[ip][regla_id]
        horas = [d['hora'] for d in datos]
        bytes_ = [d['bytes'] for d in datos]

        ax.clear()
        ax.plot(horas, bytes_, marker='o')
        ax.set_title(f"{ip} - Regla {regla_id}")
        ax.set_xlabel("Hora")
        ax.set_ylabel("Bytes")
        ax.set_xticks([])
        canvas.draw()

        root.after(10000, actualizar_grafico)

    root = tk.Tk()
    root.title("Gráfico por Regla NAT")
    root.geometry("800x600")

    router_var = tk.StringVar()
    regla_var = tk.StringVar()

    ttk.Label(root, text="Seleccionar Router").pack()
    router_box = ttk.Combobox(root, textvariable=router_var, values=list(shared_data.keys()), state="readonly")
    router_box.pack()
    router_box.bind("<<ComboboxSelected>>", actualizar_reglas)

    ttk.Label(root, text="Seleccionar Regla NAT").pack()
    regla_box = ttk.Combobox(root, textvariable=regla_var, state="readonly")
    regla_box.pack()
    regla_box.bind("<<ComboboxSelected>>", actualizar_grafico)

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    root.mainloop()
