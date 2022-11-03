edad = input('Ingrese su edad\n')

if int(edad) > 18:
    print('Tu eres mayor de edad.')
elif int(edad) == 18:
    print('Tienes 18 exactos')
else:
    print('Tu eres menor de edad.')

# Hadouken, mala práctica
edad_parseada = int(edad)
if edad_parseada > 18:
    if edad_parseada == 20:
        print('Tienes 20')
        if edad_parseada == 20:
            print('Tienes 20')
            if edad_parseada == 20:
                print('Tienes 20')
                if edad_parseada == 20:
                    print('Tienes 20')
                else:
                    print('Eres mayor de edad pero no tienes 20')
            else:
                print('Eres mayor de edad pero no tienes 20')
        else:
            print('Eres mayor de edad pero no tienes 20')
    else:
        print('Eres mayor de edad pero no tienes 20')

if edad_parseada > 18:
    pass
else:
    print('No puedes entrar')


nombre = 'RaFaEl '
if nombre.upper().strip() != 'RAFAEL':
    print('Que bueno que no eres Rafael, bienvenido')
else:
    print('Qué no puedes entrar!!')