import pickle

def hacer_prediccion():
    # Cargar el modelo entrenado
    with open('modelo_ciclones.pkl', 'rb') as f:
        model = pickle.load(f)

    # Solicitar la temperatura y la humedad al usuario
    temp = float(input("Ingrese la temperatura (en grados): "))
    hum = float(input("Ingrese la humedad (en porcentaje): "))

    # Predecir la probabilidad de ciclón
    probabilidad = model.predict_proba([[temp, hum]])[0][1]
    print(f"Probabilidad de ciclón: {probabilidad * 100:.2f}%")



