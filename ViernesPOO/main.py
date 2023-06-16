from cosas import *

def main():
    per1 = Persona("José", 19)
    print(per1)
    print(Persona.descripcion)

    print("--Herencia almuno---")
    al1 = Alumno("José", 19, "889983789", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Jaun"
    print(al2)
    al2.dormir()

    print("---herencia profesor")
    profe1 = Profesor("Jesus", 30 + 16, 67326753, "Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("----Herencia ayudante profe")
    ayudante = AyudanteProfesor("Adrián", 20, "35263", "ICO", 3675236, "Ingenieria de software", 4)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")

main()