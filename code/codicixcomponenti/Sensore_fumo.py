from machine import ADC, Pin
import time

class SensoreFumo:
    def __init__(self, pin_ao=1, pin_do=2, soglia=900):
        """
        Inizializza il sensore di fumo per ESP32-S3.
        
        NOTE PER S3:
        :param pin_ao: GPIO 1 (Molte schede S3 hanno l'ADC1 sul GPIO 1)
        :param pin_do: GPIO 2 (GPIO standard per input digitale)
        :param soglia: Valore soglia per l'allarme software
        """
        # Configurazione Analogica su ESP32-S3
        # Usiamo il pin 1 che è un pin ADC1 standard per S3
        self.adc = ADC(Pin(pin_ao))
        
        # L'attenuazione 11dB permette di leggere fino a ~3.9V 
        # Fondamentale se il sensore riceve 5V ma lo S3 lavora a 3.3V 
        # (Attenzione: Non superare i 3.3V sul pin dell'S3!)
        self.adc.atten(ADC.ATTN_11DB)
        
        # Configurazione Digitale
        self.do_pin = Pin(pin_do, Pin.IN)
        
        self.soglia = soglia

    def _leggi_media(self, campioni=10):
        totale = 0
        for _ in range(campioni):
            totale += self.adc.read()
            time.sleep_ms(10)
        return totale // campioni

    def get_readings(self):
        valore_ao = self._leggi_media(10)
        valore_do = self.do_pin.value()
        allarme = valore_ao > self.soglia
        
        return {
            "ao": valore_ao,
            "do": valore_do,
            "allarme": allarme
        }

