# main.py
from modelo_entrenamiento import entrenar_y_guardar_modelo
from prediccion_ciclones import hacer_prediccion

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Generar datos")
        print("2. Entrenar modelo")
        print("3. Hacer predicción de ciclón")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == '1':
            from data_generator import generar_datos
            try:
                generar_datos()
                print("Datos generados correctamente y guardados en 'datos_ciclones.xlsx'.")
            except Exception as e:
                print(f"Ocurrió un error al generar los datos o guardar el archivo Excel: {e}")
        
        elif opcion == '2':
            try:
                # Verifica si el archivo existe antes de intentar cargarlo
                import os
                if os.path.exists('datos_ciclones.xlsx'):
                    entrenar_y_guardar_modelo()
                    print("Modelo entrenado y guardado exitosamente.")
                else:
                    print("El archivo 'datos_ciclones.xlsx' no existe. Por favor, genere los datos primero.")
            except Exception as e:
                print(f"Ocurrió un error durante el entrenamiento o guardado del modelo: {e}")
        
        elif opcion == '3':
            try:
                hacer_prediccion()
            except Exception as e:
                print(f"Ocurrió un error al hacer la predicción: {e}")

        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción correcta.")

if __name__ == "__main__":
    main()
