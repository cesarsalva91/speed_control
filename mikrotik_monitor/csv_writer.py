import csv, os
from datetime import datetime

def save_stats(ip, stats):
    os.makedirs("output", exist_ok=True)
    file = f"output/{ip}_nat_stats.csv"
    file_exists = os.path.exists(file)

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        # Escribimos encabezado solo si es nuevo
        if not file_exists:
            writer.writerow(["Hora", "Bytes", "ID Regla", "Comentario", "IP", "Paquetes"])

        for s in stats:
            hora = datetime.now().strftime("%H:%M:%S")
            writer.writerow([hora, s['bytes'], s['id'], s['comment'], ip, s['packets']])
