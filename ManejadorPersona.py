from claseInscripcion import Inscripcion
from clasePersona import Persona
from claseTaller import TallerCapacitacion

class ManejadorPersonas:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        self._personas.append(persona)

    def buscar_persona(self, dni):
        i = 0
        while i < len(self._personas):
            persona = self._personas[i]
            if persona._dni == dni:
                return i, persona
            i += 1
        return None, None

    def get_personas(self):
        return self._personas