"""
PARCIAL 2 - Nivel 1 (20 pts) · Framing

TCP es un flujo de bytes, no de mensajes. Cada mensaje viaja así:

    4 bytes con la longitud del cuerpo (big-endian)  +  el cuerpo en UTF-8

Complete los TODO. No cambie los nombres ni las firmas: las pruebas, el
servidor y los clientes importan estas tres funciones.

Requisitos:
  1. El prefijo es struct.pack("!I", n), donde n es la longitud EN BYTES del
     cuerpo ya codificado.
  2. recibir_exacto llama a recv() EN BUCLE hasta completar los n bytes.
  3. UTF-8 explícito al codificar y al decodificar.
  4. Si recv() devuelve bytes vacíos, la conexión se cerró: se devuelve None.

Se comprueba con:   python3 prueba_n1.py   (desde la carpeta parcial2/)
"""

import socket
import struct 

def recibir_exacto(sock: socket.socket, n: int) -> bytes | None: 
    """Lee exactamente n bytes. Devuelve None si la conexión se cerró antes."""
    datos = bytearray()
    
    while len(datos) < n:
        print(datos)

        parte = sock.recv(n - len(datos))
        if not parte:
            return None
        datos.extend(parte)
    return bytes(datos)

def enviar_mensaje(sock: socket.socket, texto: str) -> None:
    """Envía un texto en utf-8 precedido por su longitud en 4 bytes (big-endian)."""
    cuerpo = texto.encode("utf-8")
    prefijo = struct.pack("!I", len(cuerpo))
    sock.sendall(prefijo + cuerpo)

def recibir_mensaje(sock: socket.socket) -> str | None:
    """recibe el mensaje enpaquetado y lo desempaqueta y lo devuelve como texto."""
    prefijo_bytes  = recibir_exacto(sock, 4)
    if prefijo_bytes is None:

        return None

    largo = struct.unpack("!I", prefijo_bytes)[0]
    cuerpo_bytes = recibir_exacto(sock, largo)
    if cuerpo_bytes is None:
        return None

    return cuerpo_bytes.decode("utf-8")

