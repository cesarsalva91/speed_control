import time
import threading
from gui import get_user_input
from mikrotik_client import get_nat_stats
from csv_writer import save_stats
from grafico import iniciar_grafico

# Diccionario compartido: datos[IP][ID_REGLA] = lista de puntos
shared_data = {}

def monitor(routers):
    while True:
        for router in routers:
            stats = get_nat_stats(router)
            hora_actual = time.strftime("%H:%M:%S")

            if router.ip not in shared_data:
                shared_data[router.ip] = {}

            for regla in stats:
                regla_id = regla['id']
                punto = {
                    "hora": hora_actual,
                    "bytes": int(regla['bytes']),
                    "comment": regla['comment'],
                    "packets": int(regla['packets'])
                }
                # Agregar punto a la lista de esa regla
                shared_data[router.ip].setdefault(regla_id, []).append(punto)

            save_stats(router.ip, stats)

        time.sleep(4)

if __name__ == "__main__":
    routers = get_user_input()
    if routers:
        # Iniciar el hilo de monitoreo
        hilo = threading.Thread(target=monitor, args=(routers,), daemon=True)
        hilo.start()

        # Iniciar la interfaz gráfica para mostrar los datos
        time.sleep(1)  # pequeño retardo para que se empiecen a llenar los datos
        iniciar_grafico(shared_data)
