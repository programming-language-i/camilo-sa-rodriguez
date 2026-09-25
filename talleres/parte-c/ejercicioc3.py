#El programa entra en un bucle infinito de creación de procesos (o lanza un RuntimeError) porque en sistemas que usan spawn cada proceso hijo reimporta el archivo principal, ejecutando de nuevo el ProcessPoolExecutor de forma recursiva; la solución mínima es envolver la ejecución del pool dentro de la guarda if _name_ == '_main_':.

from concurrent.futures import ProcessPoolExecutor

def cuadrado(n):
    return n * n

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as pool:
        resultado = list(pool.map(cuadrado, range(4)))
        print(resultado)