import threading
import time

def imprimir_mensaje():
    for i in range(5):
        print("hello")

def main():
  
    thread = threading.Thread(target=imprimir_mensaje)
    thread.start()

    
    thread.join()

    print("finalizo")

if __name__ == "__main__":
    main()
