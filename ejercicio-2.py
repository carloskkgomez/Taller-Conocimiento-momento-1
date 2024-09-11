#ciclo o metodo for 
empleados = 1897
for i in range(1, empleados + 1):
    salario_base = float(input(f"Ingrese el salario base del empleado {i}: "))     
    porcentaje_comision = float(input(f"Ingrese el porcentaje de comisiones para el empleado {i} (ej. 10 para 10%): "))    
    comisiones = salario_base * (porcentaje_comision / 100)      
    salario_con_comisiones = salario_base + comisiones         
    seguridad_social = salario_con_comisiones * 0.08                    
    salario_total = salario_con_comisiones - seguridad_social        
    print(f"Empleado {i}: Salario base = {salario_base}, Comisiones = {comisiones}, Seguridad Social = {seguridad_social}")
    print(f"Salario total = {salario_total}\n")

#ciclo o metodo  while
empleados = 1897
i = 1
while i <= empleados:
    salario_base = float(input(f"Ingrese el salario base del empleado {i}: "))    
    # Pedimos el porcentaje de comisión como un valor del 0 al 100, por ejemplo, 10 para 10%
    porcentaje_comision = float(input(f"Ingrese el porcentaje de comisiones para el empleado {i} (ej. 10 para 10%): "))    
    # Calcular la comisión en base al salario
    comisiones = salario_base * (porcentaje_comision / 100)    
    # Sumar comisiones al salario base
    salario_con_comisiones = salario_base + comisiones    
    # Calcular la seguridad social (8% sobre el salario con comisiones)
    seguridad_social = salario_con_comisiones * 0.08    
    # Calcular el salario total después de la deducción de seguridad social
    salario_total = salario_con_comisiones - seguridad_social    
    print(f"Empleado {i}: Salario base = {salario_base}, Comisiones = {comisiones}, Seguridad Social = {seguridad_social}")
    print(f"Salario total = {salario_total}\n")    
    i += 1
