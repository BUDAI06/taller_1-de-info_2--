from monitoreo import SistemaMonitoreoSQL
from sensores.cardiaco import SensorCardiaco
from sensores.respiratorio import SensorRespiratorio
from sensores.temperatura import SensorTemperatura

def main():
    sistema = SistemaMonitoreoSQL()

    while True:
        print("\n=== SISTEMA DE MONITOREO (SQL) ===")
        print("1. Agregar sensor")
        print("2. Ver datos de un sensor")
        print("3. Contar sensores")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nTipos de sensores:")
            print("1. Cardiaco (Hz)")
            print("2. Respiratorio (L/min)")
            print("3. Temperatura (°C)")
            tipo_sensor = input("Seleccione tipo de sensor: ")

            id_sensor = input("Ingrese ID del sensor: ")

            if tipo_sensor == "1":
                tipo = "Cardiaco"
                unidad = "Hz"
                frecuencia = float(input("Ingrese frecuencia de muestreo (Hz): "))
                sensor = SensorCardiaco(id_sensor, tipo, unidad, frecuencia)

            elif tipo_sensor == "2":
                tipo = "Respiratorio"
                unidad = "L/min"
                capacidad = float(input("Ingrese capacidad de flujo (L/min): "))
                sensor = SensorRespiratorio(id_sensor, tipo, unidad, capacidad)

            elif tipo_sensor == "3":
                tipo = "Temperatura"
                unidad = "°C"
                minimo = float(input("Ingrese temperatura mínima (°C): "))
                maximo = float(input("Ingrese temperatura máxima (°C): "))
                sensor = SensorTemperatura(id_sensor, tipo, unidad, (minimo, maximo))

            else:
                print(" Opción inválida")
                continue

            sistema.agregar_sensor(sensor)
            print(" Sensor agregado en la BD.")

        elif opcion == "2":
            id_sensor = input("Ingrese el ID del sensor a consultar: ")
            sistema.ver_datos_sensor(id_sensor)

        elif opcion == "3":
            sistema.contar_sensores()

        elif opcion == "4":
            print(" Saliendo del sistema...")
            break
        else:
            print(" Opción inválida")

if __name__ == "__main__":
    main()
