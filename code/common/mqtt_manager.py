from umqtt.simple import MQTTClient

#preferisco usate i type hints per maggior controllo
class MQTTManager:
    def __init__(self, client_id: str, broker: str, port: int = 1883, user: str = None, password: str = None):
        self.broker = broker
        self.client = MQTTClient(
            client_id=client_id,
            server=broker,
            port=port,
            user=user,
            password=password,
        )

    def connect(self) -> MQTTClient:
        """Stabilisce la connessione con il broker MQTT"""
        print(f"[MQTT] Connessione a {self.broker}...")
        self.client.connect()
        print("[MQTT] Connesso!")
        return self.client

    #umqtt.simple vuole solo bytes. es: b"topic, b"payload".
    #con publish() e subscribe() nel main usiamo direttamente str
    def publish(self, topic: str, payload: str, retain: bool = False) -> None:
        """Pubblica una stringa su un topic"""
        self.client.publish(topic.encode(), payload.encode(), retain=retain)

    def subscribe(self, topic: str, callback) -> None:
        """Registra la funzione di callback e si iscrive al topic"""
        self.client.set_callback(callback)
        self.client.subscribe(topic.encode())
        print(f"[MQTT] Sottoscritto al topic: {topic}")

    def disconnect(self) -> None:
        """Chiude la connessione con il broker in sicurezza"""
        try:
            self.client.disconnect()
            print("[MQTT] Disconnesso.")
        except Exception:
            pass