from sensores.base import SensorBiomedico
class SensorCardiaco(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, frecuencia_muestreo):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__frecuencia_muestreo = frecuencia_muestreo

    def get_frecuencia_muestreo(self): return self.__frecuencia_muestreo
    def set_frecuencia_muestreo(self, valor): self.__frecuencia_muestreo = valor

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Frecuencia Muestreo (Hz)"] = self.__frecuencia_muestreo
        return datos
