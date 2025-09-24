from sensores.base import SensorBiomedico

class SensorRespiratorio(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, capacidad_flujo):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__capacidad_flujo = capacidad_flujo

    def get_capacidad_flujo(self): return self.__capacidad_flujo
    def set_capacidad_flujo(self, valor): self.__capacidad_flujo = valor

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Capacidad de Flujo (L/min)"] = self.__capacidad_flujo
        return datos
