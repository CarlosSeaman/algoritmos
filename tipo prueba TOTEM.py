import random

# Definir una lista vacía para almacenar los datos de las personas
personas = []
#definir la funcion para validar el rut (solo funcionara con rut validos)
def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    if len(rut) != 9 or not rut[:-1].isdigit():
        return False
    multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3]
    total = sum(int(digito) * multiplicador for digito, multiplicador in zip(rut[:-1][::-1], multiplicadores))
    resto = total % 11
    digito_verificador = str(11 - resto)
    if digito_verificador == "11":
        digito_verificador = "0"
    elif digito_verificador == "10":
        digito_verificador = "K"
    return rut[-1].upper() == digito_verificador
# definir funciones requeridas que se desplegaran en el menu
def imprimir_personas():
    print("Personas registradas:")
    for persona in personas:
        print(f"RUT: {persona['rut']}")
        print(f"Nombre: {persona['nombre']}")
        print(f"Edad: {persona['edad']}")
        print(f"País de nacimiento: {persona['pais_nacimiento']}")
        print(f"Ciudad de nacimiento: {persona['ciudad_nacimiento']}")
        print("-" * 20)

def grabar_persona():
    rut = input("Ingrese el RUT de la persona (formato: XX.XXX.XXX-X): ")
    while not validar_rut(rut):
        print("RUT inválido. Por favor, ingréselo nuevamente.")
        rut = input("Ingrese el RUT de la persona (formato: XX.XXX.XXX-X): ")

    nombre = input("Ingrese el nombre de la persona: ")
    while len(nombre) < 8:
        print("El nombre debe tener al menos 8 caracteres.")
        nombre = input("Ingrese el nombre de la persona: ")

    edad = int(input("Ingrese la edad de la persona: "))
    while edad < 0:
        print("La edad debe ser mayor o igual a 0.")
        edad = int(input("Ingrese la edad de la persona: "))

    pais_nacimiento = input("Ingrese el país de nacimiento de la persona: ")
    ciudad_nacimiento = input("Ingrese la ciudad de nacimiento de la persona: ")

    persona = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "pais_nacimiento": pais_nacimiento,
        "ciudad_nacimiento": ciudad_nacimiento
    }

    personas.append(persona)
    print("Datos de la persona grabados correctamente.")

def buscar_persona():
    rut = input("Ingrese el RUT de la persona a buscar: ")
    for persona in personas:
        if persona["rut"] == rut:
            print("Información de la persona:")
            print(f"RUT: {persona['rut']}")
            print(f"Nombre: {persona['nombre']}")
            print(f"Edad: {persona['edad']}")
            print(f"País de nacimiento: {persona['pais_nacimiento']}")
            print(f"Ciudad de nacimiento: {persona['ciudad_nacimiento']}")
            if persona['pais_nacimiento'].lower() == 'chile':
                print("La persona pertenece al país de Chile.")
            return

    print("No se encontró ninguna persona con ese RUT.")

def largo_lista():
    largo = len(personas)
    print(F"la cantidad de registros es : {largo}")


def imprimir_certificados():
    certificados = [
        {
            "nombre": "Certificado de Nacimiento",
            "codigo": "CN"
        },
        {
            "nombre": "Estado Conyugal",
            "codigo": "EC"
        },
        {
            "nombre": "Perteneciente a Chile",
            "codigo": "PC"
        }
    ]

    for certificado in certificados:
        print(f"Nombre del certificado: {certificado['nombre']}")
        rut = input("Ingrese el RUT de la persona: ")
        for persona in personas:
            if persona["rut"] == rut:
                print(f"RUT de la persona: {persona['rut']}")
                print(f"Nombre de la persona: {persona['nombre']}")
                print(f"Datos adicionales del certificado {certificado['codigo']}")

def eliminar_persona():
    rut = input("Ingrese el RUT de la persona a eliminar: ")
    for persona in personas:
        if persona["rut"] == rut:
            personas.remove(persona)
            print("La persona ha sido eliminada correctamente.")
            return

    print("No se encontró ninguna persona con ese RUT.")
#definir funcion menu para luego llamarla en cualquier lugar solo con el nombre y no tener que iterar sobre el menu  
def imprimir_menu():
    print("\n------ MENÚ ------")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Eliminar")
    print("5 mostrar personas guardadas")
    print("6. Salir")
    print("7. cantidad de registros")
#definimos es programa como main o principal para que se ejecute con maxima prioridad sobre otros modulos
def main():
    print("Bienvenido al programa de TOTEM de autoservicio de atención rápida")
    print("Versión 1.0\n")

    while True:
        imprimir_menu()
        opcion = input("Ingrese el número de la opción que desea seleccionar: ")

        if opcion == "1":
            grabar_persona()
        elif opcion == "2":
            buscar_persona()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            eliminar_persona()
        elif opcion == "5":
            imprimir_personas()
        elif opcion == "6":    
            print("Gracias por utilizar el programa. Hasta luego.")
            break
        elif opcion == "7":
            largo_lista()
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
#esto hara que el programa solo funcione de forma principal y no sea importado desde otro modulo 
#hara que siempre sea esta la version original del programa y queda sujeta a tus cambios de versio
if __name__ == "__main__":
    main()