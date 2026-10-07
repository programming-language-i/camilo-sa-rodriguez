import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

clientes = []
lock = threading.Lock()


def enviar_mensaje(mensaje, cliente_actual):
    print("Función de envío de mensajería")

    with lock:
        for cliente in clientes[:]:
            if cliente != cliente_actual:
                try:
                    cliente.send(mensaje.encode("utf-8"))
                except OSError:
                    print(f"Error al enviar mensaje a {cliente.getpeername()}")
                    clientes.remove(cliente)


def atender_cliente(cliente_socket, direccion):
    print(f"Cliente conectado: {direccion}")

    with lock:
        clientes.append(cliente_socket)
import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

clientes = []
lock = threading.Lock()


def enviar_mensaje(mensaje, cliente_actual):
    print("Función de envío de mensajería")

    with lock:
        for cliente in clientes[:]:
            if cliente != cliente_actual:
                try:
                    cliente.send(mensaje.encode("utf-8"))
                except OSError:
                    print(f"Error al enviar mensaje a {cliente.getpeername()}")
                    clientes.remove(cliente)


def atender_cliente(cliente_socket, direccion):
    print(f"Cliente conectado: {direccion}")

    with lock:
        clientes.append(cliente_socket)

    try:
        while True:
            mensaje = cliente_socket.recv(1024)

            if not mensaje:
                break

            mensaje = mensaje.decode("utf-8")

            print(f"{direccion}: {mensaje}")

            enviar_mensaje(
                f"{direccion}: {mensaje}",
                cliente_socket
            )

    except OSError as e:
        print(f"Error con el cliente {direccion}: {e}")

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
            target=atender_cliente,
            args=(cliente_socket, direccion)
        )

        hilo.start()