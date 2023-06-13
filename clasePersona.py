class Persona:
    __nombre='string'
    __direccion='string'
    __dni='int'
    
    def __init__(self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_dni(self):
        return self.__dni

    def __str__(self):
        return f"{self.get_nombre()} (DNI: {self.get_dni()}) - Dirección: {self.get_direccion()}"


    

