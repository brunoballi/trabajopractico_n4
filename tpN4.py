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

nota1 = int(input("ingrese nota del primer parcial"))
nota2 = int(input("ingrese nota del segundo parcial"))
nota3 = int(input("ingrese nota del tercer parcial"))
if nota3 >= 6:
    promedio = (nota1 + nota2 + nota3) // 3
    if promedio >= 6:
        print("El promedio del alumno es: ",promedio)
        print("La nota del Tercer parcial supera el 6.\nTercer parcial =",nota3)
        print("MATERIA APROBADA")
    else:
        print("No aprobado el promedio es: ",promedio)
else:
    print("No aprobado.La nota del TERCER PARCIAL debe ser mayor o igual a 6.")
