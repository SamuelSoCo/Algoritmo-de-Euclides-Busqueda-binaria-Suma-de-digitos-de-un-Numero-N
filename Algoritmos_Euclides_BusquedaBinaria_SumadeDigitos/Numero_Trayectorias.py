from itertools import combinations
import math
import sys

# Límites para controlar cuántos caminos mostrar
LIMITE_MOSTRAR_TODOS = 10000   # Si hay menos de este número, se muestran todos
LIMITE_MOSTRAR_PARCIAL = 1000  # Si hay más de LIMITE_MOSTRAR_TODOS, se pueden mostrar hasta este número

def calcular_caminos(origen, destino):
    """
    Calcula el número total de caminos posibles moviéndose solo hacia la derecha (R)
    y hacia arriba (U) desde un punto de origen hasta un punto destino.
    Devuelve el número total y una lista con los caminos si son pocos.
    """

    x_inicio, y_inicio = origen
    x_fin, y_fin = destino

    pasos_derecha = x_fin - x_inicio
    pasos_arriba = y_fin - y_inicio

    # Validación de coordenadas
    if pasos_derecha < 0 or pasos_arriba < 0:
        raise ValueError("El destino debe estar a la derecha y/o arriba del origen.")

    # Si origen y destino son iguales, no hay caminos
    if pasos_derecha == 0 and pasos_arriba == 0:
        return 0, []

    # Número total de caminos: (pasos_derecha + pasos_arriba) C pasos_derecha
    total_caminos = math.comb(pasos_derecha + pasos_arriba, pasos_derecha)

    # Si el total es pequeño, generamos todas las rutas
    if total_caminos <= LIMITE_MOSTRAR_TODOS:
        lista_caminos = generar_todos_los_caminos(pasos_derecha, pasos_arriba)
        return total_caminos, lista_caminos
    else:
        # Si hay demasiados caminos, solo devolvemos el número
        return total_caminos, []


def generar_todos_los_caminos(pasos_derecha, pasos_arriba):
    """
    Genera todas las rutas posibles como cadenas de 'R' y 'U'.
    Usa combinaciones para evitar duplicados y mejorar eficiencia.
    """
    total_pasos = pasos_derecha + pasos_arriba
    caminos = []

    # Las combinaciones determinan en qué posiciones irán las 'R'
    for posiciones_r in combinations(range(total_pasos), pasos_derecha):
        ruta = ['U'] * total_pasos
        for i in posiciones_r:
            ruta[i] = 'R'
        caminos.append(''.join(ruta))

    return caminos


def leer_entero(mensaje):
    """Pide al usuario un número entero válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número entero válido.")


# Programa principal
x_inicio = leer_entero("Ingresa la coordenada x inicial: ")
y_inicio = leer_entero("Ingresa la coordenada y inicial: ")
x_fin = leer_entero("Ingresa la coordenada x final: ")
y_fin = leer_entero("Ingresa la coordenada y final: ")

try:
    total_caminos, lista_caminos = calcular_caminos((x_inicio, y_inicio), (x_fin, y_fin))
except ValueError as error:
    print("Error:", error)
    sys.exit(1)

print(f"\nNúmero total de caminos posibles: {total_caminos}")

# Si no hay caminos (origen = destino)
if total_caminos == 0:
    print("El origen y el destino son iguales, no hay caminos por recorrer.")
    sys.exit(0)

# Si hay pocos caminos, se muestran todos
if lista_caminos:
    print("\nCaminos posibles:")
    for indice, camino in enumerate(lista_caminos, start=1):
        print(f"{indice}. {camino}")
else:
    # Si hay demasiados caminos, se pregunta si se quieren ver algunos
    print("\nHay demasiados caminos para mostrar todos.")
    respuesta = input("¿Deseas ver algunos ejemplos? (s/n): ").strip().lower()

    if respuesta == 's':
        while True:
            try:
                cantidad = int(input(f"¿Cuántos caminos deseas ver? (máximo {LIMITE_MOSTRAR_PARCIAL}): "))
                if cantidad <= 0:
                    print("Debe ser un número mayor que 0.")
                    continue
                if cantidad > LIMITE_MOSTRAR_PARCIAL:
                    print(f"Se mostrarán solo los primeros {LIMITE_MOSTRAR_PARCIAL} caminos.")
                    cantidad = LIMITE_MOSTRAR_PARCIAL
                break
            except ValueError:
                print("Introduce un número entero válido.")

        pasos_derecha = x_fin - x_inicio
        pasos_arriba = y_fin - y_inicio
        total_pasos = pasos_derecha + pasos_arriba

        print(f"\nMostrando los primeros {cantidad} caminos (de un total de {total_caminos}):")
        contador = 0

        for posiciones_r in combinations(range(total_pasos), pasos_derecha):
            ruta = ['U'] * total_pasos
            for i in posiciones_r:
                ruta[i] = 'R'
            contador += 1
            print(f"{contador}. {''.join(ruta)}")
            if contador >= cantidad:
                break
    else:
        print("No se mostrarán caminos.")
