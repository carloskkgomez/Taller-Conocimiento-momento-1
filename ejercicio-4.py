#ciclo for
for i in range(2):
    puntaje = int(input(f"Ingrese el puntaje de leucemia del paciente {i+1}: "))
    if puntaje <= 10:
        nivel = "No tiene leucemia"
    elif 11 <= puntaje <= 40:
        nivel = "Nivel bajo de leucemia"
    elif 41 <= puntaje <= 69:
        nivel = "Nivel moderado de leucemia"
    elif 70 <= puntaje <= 100:
        nivel = "Nivel grave de leucemia"
    else:
        nivel = "Puntaje fuera de rango"
    
    print(f"Paciente {i+1}: {nivel}")

#ciclo while
i = 0
pacientes = 803

while i < pacientes:
    puntaje = int(input(f"Ingrese el puntaje de leucemia del paciente {i+1}: "))
    if puntaje <= 10:
        nivel = "No tiene leucemia"
    elif 11 <= puntaje <= 40:
        nivel = "Nivel bajo de leucemia"
    elif 41 <= puntaje <= 69:
        nivel = "Nivel moderado de leucemia"
    elif 70 <= puntaje <= 100:
        nivel = "Nivel grave de leucemia"
    else:
        nivel = "Puntaje fuera de rango"
    
    print(f"Paciente {i+1}: {nivel}")
    i += 1
