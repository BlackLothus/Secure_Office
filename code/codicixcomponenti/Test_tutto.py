import network
import time
from umqtt.simple import MQTTClient
from ConnessioneMQTT import Connessionemqtt
import dht
import ujson
import machine
from Led import Led


def cambio_stato(msg):
    if (msg==b'1'):
        led.on()
    elif(msg==b'0'):
        led.off()
        

# 1. Creazione dell'istanza della classe
gestore = Connessionemqtt(
    ssid="TIM-28817030",
    password="tdQstCGHtQyezTDkz5NY5uHA",
    mqtt_broker="192.168.137.111",
    client_id="Esp32_mittente",
    topic=b"iot37/corso/controllo_dht",
    mqtt_port=1883,
    wifi_timeout=60,
)
pin_dht = machine.Pin(4)
led=Led(19)
# Crea l'oggetto sensore DHT22
sensor = dht.DHT22(pin_dht)

client = gestore.connetti()
client.set_callback(cambio_stato)
client.subscribe(b"iot37/corso/led")
try:
    prev=""
    while True:
        print("misuro dati in lettura") # Il DHT22 richiede almeno 2 secondi tra una lettura e l'altra
        time.sleep(2)        
        # Avvia la misurazione
        sensor.measure()        
        # Leggi temperatura e umidità
        temp = sensor.temperature()
        hum = sensor.humidity()
        message=ujson.dumps(
            {
            "temp": temp,
             "humidity" : hum,               
            })
        if(message!=prev):
            print(f"Temperatura: {temp:.1f} °C  |  Umidità: {hum:.1f}%")
            client.publish(gestore.topic,message)
            client.wait_msg()
            prev=message
            
        
    

  
except Exception as e:
    print("Errore durante il test:", e)
