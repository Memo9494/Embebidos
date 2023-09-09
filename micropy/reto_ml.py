import pickle
from utime import localtime

# Función para cargar el modelo
def cargar_modelo(ruta):
    with open(ruta, 'rb') as f:
        return pickle.load(f)

# Función para realizar una predicción basada en la hora actual
def hacer_prediccion(modelo, hora_actual):
    # Preparar la hora actual para hacer una predicción
    hora_para_prediccion = [[hora_actual]]
    return modelo.predict(hora_para_prediccion)[0]

# Ruta al archivo del modelo
ruta_modelo = 'modelo_neuronal.pkl'

# Cargar el modelo
modelo = cargar_modelo(ruta_modelo)

# Obtener la hora actual
hora_actual = localtime()[3]
print(f'Hora actual: {hora_actual}')

# Realizar una predicción
prediccion = hacer_prediccion(modelo, hora_actual)

print(f'Predicción de temperatura para la hora {hora_actual}: {prediccion:.2f} °C')
