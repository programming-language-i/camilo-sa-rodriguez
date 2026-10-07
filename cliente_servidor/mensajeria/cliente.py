import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

nombre = input("Ingresa tu nombre: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))


def recibir_mensajes():
    while True:
        try:
            mensaje = cliente.recv(1024)

            if not mensaje:
                break

            print("\n" + mensaje.decode("utf-8"))

        except OSError:
            break


hilo = threading.Thread(target=recibir_mensajes)
hilo.daemon = True
hilo.start()


print(f"Conectado como {nombre}")
print("Escribe tus mensajes. Escribe 'salir' para desconectarte.")

while True:
    mensaje = input()

    if mensaje.lower() == "salir":
        break

    mensaje_completo = f"{nombre}: {mensaje}"

    try:
        cliente.sendall(mensaje_completo.encode("utf-8"))
    except OSError:
        print("No se pudo enviar el mensaje.")
        break