from machine import ADC, Pin
import time

# Configurazione AO sul Pin 34
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)

# Configurazione DO sul Pin 33
do_pin = Pin(33, Pin.IN)

# Soglia software impostata sopra la baseline (aria pulita ~570)
SOGLIA_FUMO = 900 

def leggi_media(campioni=10):
    totale = 0
    for _ in range(campioni):
        totale += adc.read()
        time.sleep_ms(10)
    return totale // campioni

print("Sensore stabilizzato e calibrato. Avvio monitoraggio...")

while True:
    # 1. Lettura analogica filtrata (media)
    valore_ao = leggi_media(10)
    
    # 2. Lettura digitale (stato del potenziometro)
    valore_do = do_pin.value()

    print(f"AO Medio: {valore_ao} | D0 (Pin 33): {valore_do}")

    # 3. Controllo della soglia software
    if valore_ao > SOGLIA_FUMO:
        print("🚨 [ATTENZIONE] Rilevato fumo o gas! Valore sopra la soglia.")

    time.sleep(1)