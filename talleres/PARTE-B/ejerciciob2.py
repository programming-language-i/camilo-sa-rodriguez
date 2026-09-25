### B2. Daemon con `finally`Un hilo daemon (de fondo) muere automáticamente en el momento exacto en que el hilo principal finaliza. Como el programa principal solo espera 0.5 s con time.sleep(0.5) antes de imprimir "fin" y terminar, la ejecución del hilo daemon se corta a la fuerza a los 0.5 s. Por esta razón, no alcanza a cumplir los 2 s necesarios para imprimir "guardado" ni se ejecuta el bloque finally ("archivo cerrado").


import threading
import time


def guardar():
    try:
        time.sleep(2)
        print("guardado")
    finally:
        print("archivo cerrado")


threading.Thread(target=guardar, daemon=True).start()
time.sleep(0.5)
print("fin")