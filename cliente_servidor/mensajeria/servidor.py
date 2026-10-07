import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

clientes = []
lock = threading.Lock()


def enviar_mensajes(mensaje, cliente_actual=None):
    print("Función de atención de mensajes")

    with lock:
        for cliente in clientes:
            if cliente != cliente_actual:
                try:
                    cliente.sendall(mensaje)
                except OSError:
                    print("Error al enviar el mensaje")


def atender_clientes(cliente_socket, direccion):
    print(f"Cliente conectado: {direccion}")

    with lock:
        clientes.append(cliente_socket)

    try:
        while True:
            mensaje = cliente_socket.recv(1024)

            if not mensaje:
                break

            print(f"Mensaje recibido: {mensaje.decode()}")

            enviar_mensajes(mensaje, cliente_socket)

    except OSError:
        print(f"Error con el cliente: {direccion}")

    finally:
        with lock:
            if cliente_socket in clientes:
                clientes.remove(cliente_socket)

        cliente_socket.close()
        print(f"Cliente desconectado: {direccion}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        cliente_socket, direccion = servidor.accept()

        hilo = threading.Thread(
            target=atender_clientes,
            args=(cliente_socket, direccion)
        )

        hilo.start()