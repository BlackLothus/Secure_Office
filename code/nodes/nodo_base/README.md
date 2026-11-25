# Nodo Base (Pavimento)

## Cosa fa
Monitora la presenza e il livello dell'acqua a terra, attivando una pompa di risucchio per il drenaggio quando necessario (con eventuale rilevazione della luminosità).

## Componentistica
*(Nota: l'elenco è provvisorio e può variare in corso d'opera)*
* **Microcontrollore:** ESP32
* **Sensori:** Sensore di livello dell'acqua, fotoresistenza *(in forse)*
* **Attuatore:** Pompa di risucchio/drenaggio

## File attesi
* `main.py`: Logica principale del nodo
* `secrets.example.py`: Template credenziali Wi-Fi e MQTT
* `water_sensor.py`:Lettura del sensore di livello dell'acqua (ed eventuale fotoresistenza)
* `pump.py` :Controllo attivazione/spegnimento della pompa di risucchio