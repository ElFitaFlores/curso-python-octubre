# ==
color = 'azul'
print(color == 'azul')
print(color == 'rojo')

# !=
print(color != 'rojo')

# >
altura = 150
altura_minima = 150
print(altura > altura_minima)

# <
print(altura < altura_minima)

# >=
print(altura >= altura_minima)

precio = 100
IVA = 0.12
impuesto = precio * IVA
impuesto = precio * IVA
print(impuesto)

# <=
print(altura <= altura_minima)


def abrir_puerta(altura, edad):
    ALTURA_MINIMA = 150
    EDAD_MINIMA = 15
    EDAD_MAXIMA = 80

    if altura <= ALTURA_MINIMA:
        print('No alcanza')
        return

    if edad <= EDAD_MINIMA:
        print('Muy joven')
        return

    if edad >= EDAD_MAXIMA:
        print('Muy grande')
        return
        
    print('Pase adelante')

abrir_puerta(140, 14)
