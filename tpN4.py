#-------------------------------------------------------------------------------
#
# 2)Una facultad toma tres parciales a sus alumnos.Para aprobar:
#   - El promedio debe ser mayor o igual a 6.
#   - La nota del tercer parcial debe ser mayor o igual que 6.
#   Hacer un programa que permita al docente ingresar las notas de los tres parci-
#   ales de un alumno. Ademas debe mostrar el promedio del alumno e indicar si
#   aprobo o no la materia.
#
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#Aqui damos un mensaje de bienvenida
print("Bienvenido al sistema de profesores de la escuela X")
#Pedimos que ingrese nombre y apellido del alumno para identificarlo
alumno= input("Ingrese el nombre y apellido del alumno: ")
#Un mensaje de instrucción:
print("A continuación, deberá ingresar la Materia que debe calcular, y luego las tres notas del alumno", alumno)
#Agregamos la variable materia:
materia= input("Ingrese el nombre de la materia: ")

nota1 = float(input("ingrese nota del primer parcial (1 al 10): "))
nota2 = float(input("ingrese nota del segundo parcial (1 al 10): "))
nota3 = float(input("ingrese nota del tercer parcial (1 al 10): "))
promedio=(nota1+nota2+nota3)/3

#Agregamos la funcion aprobado
def aprobado():
    print("El promedio del alumno: ", alumno, "es: ",promedio)
    print(alumno,"Aprobó: ", materia)

if nota3 >= 6:
    if promedio >= 6:
         aprobado()
    else:
        print("El alumno: ", alumno, ",obtuvo un promedio de: ",promedio, ".No esta aprobado")  
else:
    print("No aprobado.La nota del TERCER PARCIAL debe ser mayor o igual a 6.")

    