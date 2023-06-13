import csv
from datetime import datetime
from claseInscripcion import Inscripcion
from clasePersona import Persona
from claseTaller import TallerCapacitacion
from ManejadorInscripcion import ManejadorInscripciones
from ManejadorPersona import ManejadorPersonas

def cargar_talleres(archivo):
    talleres = []
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            idTaller, nombre, vacantes, montoInscripcion = int(row[0]), row[1], int(row[2]), int(row[3])
            taller = TallerCapacitacion(idTaller, nombre, vacantes, montoInscripcion)
            talleres.append(taller)
    return talleres

def inscribir_persona(persona, taller, manejador_personas, manejador_inscripciones):
    fechaInscripcion = datetime.now().strftime('%Y-%m-%d')
    inscripcion = Inscripcion(fechaInscripcion, False, persona, taller)
    manejador_inscripciones.agregar_inscripcion(inscripcion)
    manejador_personas.agregar_persona(persona)
    taller.actualizar_vacantes(1)

def main():
    archivo_talleres = "Talleres.csv"
    talleres = cargar_talleres(archivo_talleres)

    manejador_personas = ManejadorPersonas()
    manejador_inscripciones = ManejadorInscripciones(100)

    while True:
        print("Menú de opciones:")
        print("1. Inscribir una persona en un taller: Se registra la inscripción (con el atributo pago en False) y la cantidad de vacantes del taller debe ser actualizada ")
        print("2. Consultar inscripción: Ingresar el DNI de una persona, si está inscripta mostrar el nombre del taller en el que se inscribió y el monto que adeuda ")
        print("3. Consultar inscriptos: Ingresar el identificador de un taller y listar los datos de los alumnos que se inscribieron en él ")
        print("4. Registrar pago: Ingresar el DNI de una persona y registrar el pago (dar al atributo pago el valor True) ")
        print("5. Guardar inscripciones: Generar un nuevo archivo que contenga los siguientes datos de las inscripciones: DNI de la persona, idTaller, fechaInscripcion y pago ")
        print("6. Salir")
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre de la persona: ")
            direccion = input("Ingrese la dirección de la persona: ")
            dni = input("Ingrese el DNI de la persona: ")
            persona = Persona(nombre, direccion, dni)

            print("Seleccione el taller:")
            for taller in talleres:
                print(f"{taller.get_idTaller()}. {taller.get_nombre()}")
            id__taller = int(input("Ingrese el ID del taller: "))
            taller = next((t for t in talleres if t.get_idTaller() == id__taller), None)

            if taller:
                inscribir_persona(persona, taller, manejador_personas, manejador_inscripciones)
                print("Inscripción realizada con éxito.")
            else:
                print("Taller no encontrado.")

        elif opcion == 2:
            dni = input("Ingrese el DNI de la persona: ")
            inscripcion = manejador_inscripciones.buscar_inscripcion(dni)
            if inscripcion:
                print(f"Inscrito en: {inscripcion.get_taller().get_nombre()} - Monto adeudado: {inscripcion.get_taller().get_montoInscripcion()}")
            else:
                print("No se encontró la inscripción.")

        elif opcion == 3:
            idTaller = int(input("Ingrese el ID del taller: "))
            inscriptos = manejador_inscripciones.listar_inscriptos(idTaller)
            print(f"Inscriptos en el taller {idTaller}:")
            for inscripcion in inscriptos:
                print(inscripcion.get_persona())

        elif opcion == 4:
            dni = input("Ingrese el DNI de la persona: ")
            inscripcion = manejador_inscripciones.buscar_inscripcion(dni)
            if inscripcion:
                inscripcion.registrar_pago()
                print("Pago registrado con éxito.")
            else:
                print("No se encontró la inscripción.")

        elif opcion == 5:
            manejador_inscripciones.guardar_inscripciones("inscripcion.csv")
            print("Inscripciones guardadas con éxito.")

        elif opcion == 6:
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
    