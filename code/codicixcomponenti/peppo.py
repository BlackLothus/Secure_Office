import dht
import machine
import time

# Inizializza il pin dati collegato al DHT22 (es. GPIO 4)
# Sull'ESP32-S3 quasi tutti i pin digitali vanno bene (evita i pin riservati come GPIO 0 o quelli flash/strapped se possibile)
pin_dht = machine.Pin(4)

# Crea l'oggetto sensore DHT22
sensor = dht.DHT22(pin_dht)

print("Avvio lettura DHT22 su ESP32-S3...")

while True:
    try:
        # Il DHT22 richiede almeno 2 secondi tra una lettura e l'altra
        time.sleep(2)
        
        # Avvia la misurazione
        sensor.measure()
        
        # Leggi temperatura e umidità
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print(f"Temperatura: {temp:.1f} °C  |  Umidità: {hum:.1f}%")
        
    except OSError as e:
        print("Errore di comunicazione con il sensore:", e)
    except Exception as e:
        print("Si è verificato un errore inatteso:", e)