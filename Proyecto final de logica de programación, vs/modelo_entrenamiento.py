import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

def entrenar_y_guardar_modelo():
    # Cargar el archivo Excel
    df = pd.read_excel('datos_ciclones.xlsx')

    # Asignar las variables de entrada (X) y la etiqueta (y)
    X = df[['temperatura', 'humedad']]
    y = df['ciclon']

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el modelo (puedes cambiar a DecisionTreeClassifier si prefieres)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo: {accuracy * 100:.2f}%')

    # Guardar el modelo en un archivo .pkl
    with open('modelo_ciclones.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Modelo entrenado y guardado exitosamente.")
