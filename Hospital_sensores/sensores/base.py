class SensorBiomedico:
    def __init__(self, id_sensor, tipo, unidad_medida):
        self.__id_sensor = id_sensor
        self.__tipo = tipo
        self.__unidad_medida = unidad_medida

    
    def get_id_sensor(self): return self.__id_sensor
    def get_tipo(self): return self.__tipo
    def get_unidad_medida(self): return self.__unidad_medida

    
    def set_id_sensor(self, id_sensor): self.__id_sensor = id_sensor
    def set_tipo(self, tipo): self.__tipo = tipo
    def set_unidad_medida(self, unidad): self.__unidad_medida = unidad

    def mostrar_datos(self):
        return {
            "ID Sensor": self.__id_sensor,
            "Tipo": self.__tipo,
            "Unidad de Medida": self.__unidad_medida
        }
