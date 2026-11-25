# Nodo Porta

## Cosa fa
Gestisce il controllo accessi tramite inserimento di un PIN su tastierino, aziona il blocco/sblocco della porta con feedback visivo e invia i frame video al PC per il monitoraggio.

## Componentistica
*(Nota: l'elenco è provvisorio e può variare in corso d'opera)*
* **Microcontrollore principale:** ESP32
* **Modulo video:** ESP32-CAM (dedicata all'invio dei frame al PC)
* **Input:** Tastierino numerico a matrice 3x4
* **Attuatore:** Servomotore (meccanismo di blocco porta)
* **Indicatori:** 2 LED di stato

## File attesi
* `main.py`: Logica principale e coordinamento del nodo
* `secrets.example.py`-:Template credenziali Wi-Fi e MQTT
* `keypad.py`: Gestione lettura matrice 3x4
* `door_lock.py`:Controllo del servomotore e dei LED di stato
* `cam_stream.py`*(o sottocartella dedicata)*: Codice per l'invio dei frame dalla ESP32-CAM