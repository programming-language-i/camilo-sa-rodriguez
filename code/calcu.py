def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b


resultado_suma = suma(2,5)
resultado_resta = resta(2,5)
resultado_multi =  multi(2,5)

print(f"resultado suma:{resultado_suma}")
print(f"resultado resta:{resultado_resta}")
print(f"resultado multiplicacion:{resultado_multi}")
print(f"resultado suma:{resultado_suma}")
























import threading
import time

def tarea(n):
    time.sleep(1)

inicio = time.perf_counter()

hilos = []
for i in range(3):
    hilo = threading.Thread(target=tarea, args=(i,))
    hilo.start()          # arranca todos
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()            # espera a todos al final

print(f"{time.perf_counter() - inicio:.1f} s")  # ~1.0 s