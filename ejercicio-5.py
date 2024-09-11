#ciclo o metodo for
for i in range(4):
    puntaje = int(input(f"Ingrese el puntaje de la cabina {i+1}: "))
    if puntaje == 2:
        estado = "Funcionamiento defectuoso"
    elif puntaje == 3:
        estado = "Funcionamiento moderado"
    elif puntaje == 4:
        estado = "Funcionamiento óptimo"
    else:
        estado = "Puntaje no válido"
    
    print(f"Cabina {i+1}: {estado}")

#ciclo o metodo  while
for i in range(407):
    puntaje = int(input(f"Ingrese el puntaje de la cabina {i+1}: "))
    if puntaje == 2:
        estado = "Funcionamiento defectuoso"
    elif puntaje == 3:
        estado = "Funcionamiento moderado"
    elif puntaje == 4:
        estado = "Funcionamiento óptimo"
    else:
        estado = "Puntaje no válido"
    
    print(f"Cabina {i+1}: {estado}")
