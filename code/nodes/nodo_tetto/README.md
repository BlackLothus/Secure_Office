# Nodo Tetto

## Cosa fa
Monitora i parametri ambientali superiori (temperatura, umidità, presenza di gas ed eventuale luce) e gestisce la ventilazione e l'erogazione dell'acqua dall'alto.

## Componentistica
*(Nota: l'elenco è provvisorio e può variare in corso d'opera)*
* **Microcontrollore:** ESP32
* **Sensori:** DHT22 (temperatura e umidità), sensore del gas,fotoresistenza *(in forse)*
* **Attuatori:** Ventola, pompa per erogazione acqua

## File attesi
* `main.py`: Logica principale del nodo
* `secrets.example.py`: Template credenziali Wi-Fi e MQTT
* `env_sensors.py`: Gestione letture DHT22, sensore gas ed eventuale fotoresistenza
* `actuators.py` :Controllo della ventola e della pompa dell'acqua