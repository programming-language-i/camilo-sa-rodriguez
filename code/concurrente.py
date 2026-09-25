import multiprocessing
import time

def print_numeros():
    for i in range(1, 5):
        print(f"Número: {i}")
        time.sleep(1)

def print_letras():
    for letra in ['A', 'B', 'C', 'D']:
        print(f"Letra: {letra}")
        time.sleep(1)

if __name__ == "__main__":
    
    proceso_numeros = multiprocessing.Process(target=print_numeros)
    proceso_letras = multiprocessing.Process(target=print_letras)

    proceso_numeros.start()
    proceso_letras.start()

    proceso_numeros.join()
    proceso_letras.join()

    print("Finalizó la ejecución de ambos procesos.")