import tkinter as tk
from tkinter import messagebox
from models import Router

def get_user_input():
    routers = []

    def actualizar_lista():
        router_list.delete(0, tk.END)
        for i, r in enumerate(routers):
            router_list.insert(tk.END, f"{i+1}. {r.ip}:{r.port} - {r.user}")

    def add_router():
        ip = ip_entry.get().strip()
        user = user_entry.get().strip()
        password = pass_entry.get().strip()
        port = port_entry.get().strip() or "8728"

        if not ip or not user or not password:
            messagebox.showwarning("Campos incompletos", "Completá todos los campos.")
            return

        try:
            port = int(port)
        except ValueError:
            messagebox.showerror("Puerto inválido", "El puerto debe ser un número.")
            return

        routers.append(Router(ip, user, password, port))
        actualizar_lista()

        ip_entry.delete(0, tk.END)
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
        port_entry.delete(0, tk.END)

    def eliminar_router():
        seleccion = router_list.curselection()
        if seleccion:
            routers.pop(seleccion[0])
            actualizar_lista()

    def iniciar():
        if not routers:
            messagebox.showerror("Sin routers", "Agregá al menos un router antes de continuar.")
            return
        root.destroy()

    root = tk.Tk()
    root.title("Carga de Routers MikroTik")
    root.geometry("400x500")
    root.resizable(False, False)

    # Campos de entrada
    tk.Label(root, text="Dirección IP").pack()
    ip_entry = tk.Entry(root, width=35)
    ip_entry.pack()

    tk.Label(root, text="Usuario").pack()
    user_entry = tk.Entry(root, width=35)
    user_entry.pack()

    tk.Label(root, text="Contraseña").pack()
    pass_entry = tk.Entry(root, width=35, show="*")
    pass_entry.pack()

    tk.Label(root, text="Puerto").pack()
    port_entry = tk.Entry(root, width=35)
    port_entry.pack()

    tk.Button(root, text="Agregar router", command=add_router).pack(pady=5)

    # Lista de routers cargados
    tk.Label(root, text="Routers agregados:").pack(pady=(10, 0))
    router_list = tk.Listbox(root, width=50, height=8)
    router_list.pack()

    tk.Button(root, text="Eliminar seleccionado", command=eliminar_router).pack(pady=5)

    # Iniciar monitoreo
    tk.Button(root, text="Iniciar monitoreo", command=iniciar, bg="green", fg="white").pack(pady=15)

    root.mainloop()
    return routers
