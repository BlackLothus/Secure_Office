import network
import time
from umqtt.simple import MQTTClient

# Credenziali Wi-Fi e MQTT
SSID = "OpenWrt"
PASSWORD = "academy2026"
MQTT_BROKER = "192.168.2.226"  # <--- METTI QUI L'IP DEL PC O DEL DISPOSITIVO CHE FA DA BROKER MQTT
CLIENT_ID = "ESP32_Mittente"
TOPIC = b"iot/academy/controllo_led"

# Connessione Wi-Fi con pulizia dello stato interno
wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(1)
wlan.active(True)
time.sleep(1)

print(f"Connessione alla rete '{SSID}' in corso...")
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConnesso al Wi-Fi! IP:", wlan.ifconfig()[0])

# Connessione MQTT
client = MQTTClient(CLIENT_ID, MQTT_BROKER)
client.connect()
print("Connesso al broker MQTT!")

# Loop: invia il comando ogni 3 secondi (o potresti collegarci un pulsante fisico)
try:
    while True:
        print("Invio comando: ACCENDI")
        client.publish(TOPIC, b"ACCENDI")
        time.sleep(3)
        
        print("Invio comando: SPEGNI")
        client.publish(TOPIC, b"SPEGNI")
        time.sleep(3)
except KeyboardInterrupt:
    client.disconnect()
    print("Disconnesso.")