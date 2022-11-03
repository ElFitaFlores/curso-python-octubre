numero = 1

while numero <= 10:
    print(numero)
    numero += 1

perros = ['Bobby', 'Rex', 'Max', 'Avellana']
for perro in perros:
    print(perro)

numero = 1
while numero <= 10:
    if numero == 5:
        break

    print(numero)
    numero += 1

perros = ['Bobby', 'Rex', 'Max', 'Avellana', 'Max', 'Max']
for perro in perros:
    if perro == 'Max':
        print('Este si es el perro')
        continue

    print('Este no es el perro')