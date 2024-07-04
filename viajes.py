from geopy.distance import distance
from geopy.geocoders import Nominatim

# Función para obtener coordenadas geográficas de una ciudad
def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(ciudad)
    if location:
        return location.latitude, location.longitude
    else:
        return None

# Función para calcular la distancia y duración del viaje
def calcular_viaje(ciudad_origen, ciudad_destino, modo_transporte):
    # Obtener coordenadas geográficas de las ciudades
    origen_coords = obtener_coordenadas(ciudad_origen)
    destino_coords = obtener_coordenadas(ciudad_destino)

    if not origen_coords or not destino_coords:
        print("No se pudieron obtener las coordenadas para las ciudades especificadas.")
        return

    # Calcular la distancia entre las coordenadas
    dist = distance(origen_coords, destino_coords).miles  # Distancia en millas

    # Estimar el tiempo de viaje según el modo de transporte
    if modo_transporte == "car":
        tiempo_minutos = dist / 60  # Suponiendo velocidad promedio de 60 millas por hora
    elif modo_transporte == "bike":
        tiempo_minutos = dist / 10  # Suponiendo velocidad promedio de 10 millas por hora
    elif modo_transporte == "foot":
        tiempo_minutos = dist / 3   # Suponiendo velocidad promedio de 3 millas por hora
    else:
        print("Modo de transporte no válido.")
        return

    return dist, tiempo_minutos

# Función principal para solicitar datos al usuario
def main():
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen en Chile: ")
        if ciudad_origen.lower() == 's':
            break
        
        ciudad_destino = input("Ingrese la ciudad de destino en Argentina: ")
        if ciudad_destino.lower() == 's':
            break
        
        modo_transporte = input("Elija el medio de transporte (car, bike, foot): ")

        distancia, tiempo_minutos = calcular_viaje(ciudad_origen, ciudad_destino, modo_transporte)

        if distancia and tiempo_minutos:
            print(f"\nDistancia del viaje: {distancia:.2f} millas")
            print(f"Tiempo estimado de viaje: {tiempo_minutos:.2f} minutos\n")
        else:
            print("No se pudo calcular la distancia y duración del viaje.\n")

if __name__ == "__main__":
    main()
