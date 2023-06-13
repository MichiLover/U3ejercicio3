class Inscripcion:
    __fechaInscripcion='int'
    __pago='bool'
    __persona='Persona'
    __taller='TallerCapacitacion'

    def __init__(self, fechaInscripcion, pago, persona, taller):
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def registrar_pago(self):
        self.__pago = True

    def get_fechaInscripcion(self):
        return self.__fechaInscripcion
    
    def get_pago(self):
        return self.__pago
    
    def get_persona(self):
        return self.__persona
    
    def get_taller(self):
        return self.__taller

    def __str__(self):
        pago_str = "Pagado" if self.__pago else "No pagado"
        return f"{self.get_persona()} - {self.get_taller()} - Fecha: {self.get_fechaInscripcion()} - {pago_str}"

