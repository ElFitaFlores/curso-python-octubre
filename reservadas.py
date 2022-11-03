def sumar():
    return 3 + 3

print("LA respuesta es: 5")

numero = sumar()

if numero == 5:
    print('Si es 5')
elif numero == 6:
    print('aah era un 6')
else:
    print('No es un 5')


x = 0
while x < 3:
    print(x)
    x += 1

print(range(3))

for i in range(3):
    print(i)

print('separacion')
for i in range(3):
    if i == 1:
        break
    print(i)

#print(True)
#print(False)


def isAdult(edad):
    return edad >= 18

print(isAdult(15))
print(isAdult(20))

#print(None)

def vacia():
    pass

print(vacia())

print(True and True)
print(True or False)
print(not True)

if not isAdult(15):
    print('no es un adulto')
