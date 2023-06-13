class TallerCapacitacion:
    __idTaller='int'
    __nombre='string'
    __vacantes='int'
    __montoInscripcion='int'
    
    def __init__(self, idTaller, nombre, vacantes, montoInscripcion):
        self.__idTaller = idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = montoInscripcion

    def actualizar_vacantes(self, cantidad):
        self.__vacantes -= cantidad

    def get_idTaller(self):
        return self.__idTaller
    
    def get_nombre(self):
        return self.__nombre
    
    def get_vacantes(self):
        return self.__vacantes
    
    def get_montoInscripcion(self):
        return self.__montoInscripcion

    def __str__(self):
        return f"{self.get_nombre()} (ID: {self.get_idTaller()}) - Vacantes: {self.get_vacantes()} - Monto: {self.get_montoInscripcion()}"



