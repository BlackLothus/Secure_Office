import network
import time


# Uso i type hints per un double check alla Java
class WiFiManager:
    def __init__(self, ssid: str, password: str, timeout_s: int = 15):
        self.ssid = ssid
        self.password = password
        self.timeout_ms = timeout_s * 1000
        self.wlan = network.WLAN(network.STA_IF)

    def _reset_interface(self) -> None:
        self.wlan.active(False)
        time.sleep_ms(500)
        self.wlan.active(True)
        time.sleep_ms(500)

    def connect(self) -> str:
        """
        Controlla se c'è già una connessione, altrimenti si connette alla rete richiesta.
        In ogni caso restituisce l'indirizzo IP assegnato.
        """
        if self.is_connected():
            return self.get_ip()

        self._reset_interface()
        print(f"[WiFi] Connessione a '{self.ssid}'...")
        self.wlan.connect(self.ssid, self.password)

        start = time.ticks_ms()
        while not self.is_connected():
            if time.ticks_diff(time.ticks_ms(), start) > self.timeout_ms:
                # Non ho implementato un retry per ora
                raise RuntimeError(f"[WiFi] Timeout connessione a '{self.ssid}'")
            print(".", end="")
            time.sleep_ms(500)

        ip = self.get_ip()
        print(f"\n[WiFi] Connesso! IP: {ip}")
        return ip

    # -- Di seguito dei metodi wrapper per la legibilità del codice --

    def is_connected(self) -> bool:
        return self.wlan.isconnected()

    def get_ip(self) -> str:
        if not self.is_connected():
            return "0.0.0.0"
        return self.wlan.ifconfig()[0]