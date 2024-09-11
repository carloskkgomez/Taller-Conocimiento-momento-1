#ciclo o metodo for
def generar_serie(n):
    serie = []
    a, b = 5, 8
    for _ in range(n):
        if a != 13:
            serie.append(a)
        a, b = b, a + b
    return serie

# ciclo while
resultado = generar_serie(101)
print(resultado)

#ciclo o metodo while
def generar_serie(n):
    serie = []
    a, b = 5, 8
    while len(serie) < n:
        if a != 13:
            serie.append(a)
        a, b = b, a + b
    return serie

# Generar los primeros 100 números de la serie sin mostrar el 13
resultado = generar_serie(100)
print(resultado)
