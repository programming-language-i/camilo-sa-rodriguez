import  threading, time

def print_numeros():
    for i in range(1, 5):
        print(f"Numero: {i}")
        time.sleep(1)

def print_letras():
    for letra in ['A', 'B', 'C', 'D']:
        print(f"Letra: {letra}")
        time.sleep(1)

if __name__ == "__main__":
    thread_numeros = threading.Thread(target=print_numeros)
    thread_letras = threading.Thread(target=print_letras)

    thread_numeros.start()
    thread_letras.start()

    thread_numeros.join()
    thread_letras.join()

    print("Finalizó la ejecución de ambos hilos.")