import threading
import time
import random

temperatura_actual = 0.0
lock = threading.Lock()

def sensor_temperatura():
    global temperatura_actual
    while True:
        nueva_temp = round(random.uniform(20.0, 35.0), 2)
        with lock:
            temperatura_actual = nueva_temp
        print(f"[Sensor] Temperatura leída: {temperatura_actual}°C")
        time.sleep(2)  # Lee cada 2 segundos

def verificar_umbral():
    while True:
        with lock:
            temp = temperatura_actual
        if temp > 30:
            print(f"  [Alerta] ¡Temperatura alta! {temp}°C")
        elif temp > 0:
            print(f" [Estado] Temperatura normal: {temp}°C")
        time.sleep(3)

def registrar_historial():
    historial = []
    while True:
        with lock:
            temp = temperatura_actual
        if temp > 0:
            historial.append(temp)
            if len(historial) > 5:  # Guarda últimos 5 valores
                historial.pop(0)
            print(f" [Registro] Últimas lecturas: {historial}")
        time.sleep(4)

def convertir_fahrenheit():
    while True:
        with lock:
            celsius = temperatura_actual
        if celsius > 0:
            fahr = round((celsius * 9/5) + 32, 2)
            print(f" [Conversor] {celsius}°C = {fahr}°F")
        time.sleep(5)

def control_ventilacion():
    estado = "APAGADO"
    while True:
        with lock:
            temp = temperatura_actual
        if temp >= 32 and estado == "APAGADO":
            estado = "ENCENDIDO"
            print("🔌 [Ventilación] → ENCENDIDA por calor")
        elif temp < 28 and estado == "ENCENDIDO":
            estado = "APAGADO"
            print("🔌 [Ventilación] → APAGADA, temperatura estable")
        time.sleep(2)

if __name__ == "__main__":  # ✅ Corrección clave
    print("=== Sistema de Monitoreo de Temperatura ===")
    print("Iniciando 5 hilos... (Presiona Ctrl+C para detener)\n")
    
    hilo1 = threading.Thread(target=sensor_temperatura, daemon=True)
    hilo2 = threading.Thread(target=verificar_umbral, daemon=True)
    hilo3 = threading.Thread(target=registrar_historial, daemon=True)
    hilo4 = threading.Thread(target=convertir_fahrenheit, daemon=True)
    hilo5 = threading.Thread(target=control_ventilacion, daemon=True)

    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()
    hilo5.start()

    # Mantener el programa activo
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Sistema detenido")