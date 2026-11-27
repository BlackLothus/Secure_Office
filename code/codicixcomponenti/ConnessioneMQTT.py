import network
import time
from umqtt.simple import MQTTClient


class Connessionemqtt:
    def __init__(self,ssid,password,mqtt_broker,client_id,topic,mqtt_port,wifi_timeout,):
        self.ssid = ssid
        self.password = password
        self.mqtt_broker = mqtt_broker
        self.client_id = client_id
        self.topic = topic
        self.mqtt_port = mqtt_port
        self.wifi_timeout = wifi_timeout
        self.wlan = network.WLAN(network.STA_IF)
        self.mqtt_client = None

    def _connetti_wifi(self):
        # Pulizia dello stato interno della scheda Wi-Fi
        self.wlan.active(False)
        time.sleep(1)
        self.wlan.active(True)
        time.sleep(1)

        print(f"Connessione alla rete '{self.ssid}' in corso...")
        self.wlan.connect(self.ssid, self.password)

        inizio = time.time()
        while not self.wlan.isconnected():
            if time.time() - inizio > self.wifi_timeout:
                raise RuntimeError(
                    f"Timeout: impossibile connettersi al Wi-Fi '{self.ssid}'"
                )
            print(".", end="")
            time.sleep(0.5)

        ip = self.wlan.ifconfig()[0]
        print(f"\nConnesso al Wi-Fi! IP: {ip}")
        return ip

    def connetti(self):
        """Esegue connessione Wi-Fi + MQTT e restituisce l'istanza MQTTClient pronta."""
        self._connetti_wifi()

        print(f"Connessione al broker MQTT '{self.mqtt_broker}:{self.mqtt_port}'...")
        self.mqtt_client = MQTTClient(
            self.client_id,
            self.mqtt_broker,
            port=self.mqtt_port,
        )
        self.mqtt_client.connect()
        print("Connesso al broker MQTT!")

        return self.mqtt_client