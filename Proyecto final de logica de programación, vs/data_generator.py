import numpy as np
import pandas as pd

def generar_datos():
    # Creando semilla para generar datos
    np.random.seed(42)

    # Número de datos a generar
    n_samples = 1000000

    # Generar datos aleatorios para temperatura y humedad
    temperaturas = np.random.uniform(low=20, high=40, size=n_samples)  # Temperatura entre 20 y 40 grados
    humedades = np.random.uniform(low=50, high=100, size=n_samples)  # Humedad entre 50% y 100%

    # Inicializar un array para ciclon, inicialmente todos 0 (sin ciclón)
    ciclon = np.zeros(n_samples)

    # Proporción de ciclones deseada (ej. 30% ciclones, 70% no ciclones)
    n_ciclones = int(n_samples * 0.3)  # 30% de ciclones

    # Elegir índices aleatorios para asignar ciclones
    indices_ciclones = np.random.choice(n_samples, n_ciclones, replace=False)

    # Asignar ciclones en esos índices
    ciclon[indices_ciclones] = 1

    # Modificar los datos de temperatura y humedad para que sean consistentes con los ciclones
    # Solo aumentar temperatura y humedad en los índices de ciclones
    temperaturas[indices_ciclones] += np.random.uniform(low=5, high=5, size=n_ciclones)  # Aumentar temperatura
    humedades[indices_ciclones] += np.random.uniform(low=5, high=5, size=n_ciclones)  # Aumentar humedad

    # Crear un DataFrame con los datos
    df = pd.DataFrame({
        'temperatura': temperaturas,
        'humedad': humedades,
        'ciclon': ciclon
    })

    # Guardar los datos en un archivo Excel
    df.to_excel('datos_ciclones.xlsx', index=False, engine='openpyxl')

# Llama a la función para generar los datos
generar_datos()
