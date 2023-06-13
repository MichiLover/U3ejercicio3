from ClaseTallerCapacitacion import TallerCapacitacion
from ClasePersona import Persona
from manejadorPersona import ManPer
from manejadorInscripcion import ManIns
from ClaseInscripcion import Inscripcion
from datetime import datetime
import csv

class ManTaller:
    __talleres = []

    def __init__(self):
        self.__talleres = []  # Arreglo para almacenar instancias de TallerCapacitacion
        self.__inscrip = ManIns()
        self.__person = ManPer()

    def cargar_talleres(self):
        archivo=open("Talleres.csv")
        reader=csv.reader(archivo,delimiter=",")
        bandera=True
        for fila in reader:

            if bandera:
                bandera=False

            else:

                id_taller = int(fila[0])
                nombre = fila[1]
                vacantes = int(fila[2])
                monto_inscripcion = float(fila[3])

                unTaller = TallerCapacitacion(id_taller, nombre, vacantes, monto_inscripcion)
                self.__talleres.append(unTaller)

    def mostrar_talleres(self):
        for taller in self.__talleres:
            print(f"ID Taller: {taller.getTaller()}, Nombre: {taller.getNom()}, Vacantes: {taller.getVacantes()}, Monto Inscripción: {taller.getMonto()}")

    def obtener_talleres(self):
        return self.__talleres

    def getPersona(self):

        return self.__person

    def getInscriptos(self):
        
        return self.__inscrip

    #ejercicio 2

    def obtener_taller_por_id(self,id_taller):
        talleres = self.obtener_talleres()
        taller_encontrado = None
        bandera=False
        i=0

        while i<len(talleres) and not bandera:
            if talleres[i].getTaller() == id_taller:
                taller_encontrado = talleres[i]
                bandera=True
            else:
                i +=1
        
        return taller_encontrado

        
    def registrar_persona(self):
        continuar = True

        while continuar:
            id_taller = int(input("Ingrese el número de taller que desea elegir (0 para salir): "))
            taller = self.obtener_taller_por_id(id_taller)

            if id_taller == 0:
                print("Saliendo del registro de personas")
                continuar = False
            elif taller is not None:
                print(f"Taller de {taller.getNom()} elegido")

                if taller.hay_vacantes():
                    fecha_inscripcion = datetime.now()
                    pago = False
                    nombre = input("Ingrese el nombre de la persona: ")
                    direccion = input("Ingrese la dirección de la persona: ")
                    dni = input("Ingrese el DNI de la persona: ")
                    unaPersona = Persona(nombre, direccion, dni)
                    inscripcion = Inscripcion(fecha_inscripcion, pago, unaPersona, taller)
                    taller.actualizar_vacantes()
                    self.__inscrip.agregar_inscripcion(inscripcion)
                    print("Inscripción exitosa")

                else:
                    print("No hay vacantes disponibles en este taller.")
            else:
                print("No se encontró un taller con ese ID.")


