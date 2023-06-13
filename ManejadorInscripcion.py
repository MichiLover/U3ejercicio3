class ManejadorInscripciones:
    def __init__(self, max_inscripciones):
        self._inscripciones = [None] * max_inscripciones
        self._cantidad_inscripciones = 0

    def agregar_inscripcion(self, inscripcion):
        if self._cantidad_inscripciones < len(self._inscripciones):
            self._inscripciones[self._cantidad_inscripciones] = inscripcion
            self._cantidad_inscripciones += 1
            return True
        return False

    def buscar_inscripcion(self, dni):
        i = 0
        while i < self._cantidad_inscripciones:
            inscripcion = self._inscripciones[i]
            if inscripcion.get_persona().get_dni() == dni:
                return inscripcion
            i += 1
        return None

    def get_inscripciones(self):
        return self._inscripciones[:self._cantidad_inscripciones]

    def listar_inscriptos(self, idTaller):
        inscriptos = []
        i = 0
        while i < self._cantidad_inscripciones:
            inscripcion = self._inscripciones[i]
            if inscripcion.get_taller().get_idTaller() == idTaller:
                inscriptos.append(inscripcion)
            i += 1
        return inscriptos

    def guardar_inscripciones(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            for inscripcion in self._inscripciones:
                if inscripcion is not None:
                    pago_str = "1" if inscripcion.get_pago() else "0"
                    f.write(f"{inscripcion.get_persona().get_dni()},{inscripcion.get_taller().get_idTaller()},{inscripcion.get_fechaInscripcion()},{pago_str}\n")



