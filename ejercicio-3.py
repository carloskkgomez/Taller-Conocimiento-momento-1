#ciclo  o metodo for 
numeros = [int(input(f"Ingrese el número {i+1}: "))
           for i in range(400)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(f"Números pares: {len(pares)}")
print(f"Números impares: {len(impares)}")

#ciclo o metodo  while
numeros = []
i = 0

# Ingresar 400 números usando un ciclo while
while i < 400:
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    i += 1
# Separar los números en pares e impares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
# Imprimir la cantidad de números pares e impares
print(f"Números pares: {len(pares)}")
print(f"Números impares: {len(impares)}")

