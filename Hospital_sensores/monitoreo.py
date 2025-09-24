from conexion import get_connection

class SistemaMonitoreoSQL:
    def __init__(self):
        self.db = get_connection()
        self.cursor = self.db.cursor()

    def agregar_sensor(self, sensor):
        datos = sensor.mostrar_datos()
        extra = (datos.get("Frecuencia Muestreo (Hz)") or
                 datos.get("Capacidad de Flujo (L/min)") or
                 str(datos.get("Rango de Operación")))

        try:
            self.cursor.execute("""
                INSERT INTO sensores (id_sensor, tipo, unidad_medida, atributo_extra)
                VALUES (%s, %s, %s, %s)
            """, (
                sensor.get_id_sensor(),
                sensor.get_tipo(),
                sensor.get_unidad_medida(),
                extra
            ))
            self.db.commit()
            print("Sensor agregado en la BD.")
        except Exception as e:
            print(f" Error al insertar: {e}")

    def ver_datos_sensor(self, id_sensor):
        self.cursor.execute("SELECT * FROM sensores WHERE id_sensor=%s", (id_sensor,))
        sensor = self.cursor.fetchone()
        if sensor:
            print(f"ID: {sensor[0]}, Tipo: {sensor[1]}, Unidad: {sensor[2]}, Extra: {sensor[3]}")
        else:
            print("Sensor no encontrado.")

    def contar_sensores(self):
        self.cursor.execute("SELECT COUNT(*) FROM sensores")
        total = self.cursor.fetchone()[0]
        return total

