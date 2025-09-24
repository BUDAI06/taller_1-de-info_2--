from monitoreo import SistemaMonitoreoSQL
from sensores.cardiaco import SensorCardiaco
from sensores.respiratorio import SensorRespiratorio
from sensores.temperatura import SensorTemperatura

def main():
    sistema = SistemaMonitoreoSQL()

    while True:
        print("\n=== SISTEMA DE MONITOREO  ===")
        print("1. Agregar sensor")
        print("2. Ver datos de un sensor")
        print("3. Contar sensores")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nTipos de sensores:")
            print("1. Cardiaco")
            print("2. Respiratorio")
            print("3. Temperatura")
            tipo = input("Seleccione tipo de sensor: ")

            id_sensor = input("Ingrese ID del sensor: ")
            tipo_sensor = input("Ingrese tipo (ej: temperatura, presión, etc.): ")
            unidad = input("Ingrese unidad de medida: ")

            if tipo == "1":
                frec = float(input("Ingrese frecuencia de muestreo (Hz): "))
                sensor = SensorCardiaco(id_sensor, tipo_sensor, unidad, frec)
            elif tipo == "2":
                flujo = float(input("Ingrese capacidad de flujo (L/min): "))
                sensor = SensorRespiratorio(id_sensor, tipo_sensor, unidad, flujo)
            elif tipo == "3":
                min_r = float(input("Ingrese rango mínimo: "))
                max_r = float(input("Ingrese rango máximo: "))
                sensor = SensorTemperatura(id_sensor, tipo_sensor, unidad, (min_r, max_r))
            else:
                print("Tipo inválido.")
                continue

            sistema.agregar_sensor(sensor)

        elif opcion == "2":
            id_buscar = input("Ingrese el ID del sensor a consultar: ")
            sistema.ver_datos_sensor(id_buscar)

        elif opcion == "3":
            print(f" Total de sensores: {sistema.contar_sensores()}")

        elif opcion == "4":
            print(" Saliendo del sistema...")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()
