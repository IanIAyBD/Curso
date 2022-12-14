# Importamos la biblioteca de noise
import noise

# Definimos el tamaño del mapa
MAP_WIDTH = 100
MAP_HEIGHT = 100

# Generamos el mapa de Perlin utilizando la biblioteca de noise
perlin_map = noise.perlin_map(MAP_WIDTH, MAP_HEIGHT, scale=0.1, octaves=4, persistence=0.5)

# Aplicamos el suavizado al mapa utilizando el método smooth()
smooth_map = noise.smooth(perlin_map)