from sensores.base import SensorBiomedico

class SensorTemperatura(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, rango_operacion):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__rango_operacion = rango_operacion  # tupla (min, max)

    def get_rango_operacion(self): return self.__rango_operacion
    def set_rango_operacion(self, rango): self.__rango_operacion = rango

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Rango de Operación"] = self.__rango_operacion
        return datos
