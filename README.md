# speed_control
Extracción y Registro de Consumo de Reglas NAT
El sistema realiza la extracción periódica de datos de reglas de NAT (Network Address Translation) en equipos MikroTik, utilizando la API de RouterOS. La información recolectada corresponde al tráfico de datos en bytes consumido por cada regla de NAT configurada en los dispositivos. Estos datos permiten monitorear el uso de internet asociado a cada regla, lo cual puede reflejar el consumo de distintos servicios, usuarios o segmentos de red.

Los valores extraídos se almacenan de forma estructurada en un archivo CSV, registrando en cada fila el identificador de la regla, la dirección IP del router correspondiente, la marca de tiempo (fecha y hora exacta de la captura), y la cantidad de bytes consumidos acumulados hasta ese momento.
