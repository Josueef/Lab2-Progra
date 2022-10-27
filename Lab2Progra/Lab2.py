def opcion():
    while not (opcion == '6'):
        print(' 1. menu opcion 01')
        print(' 2. menu opcion 02')
        print(' 3. menu opcion 03')
        print(' 4. menu opcion 04')
        print(' 5. menu opcion 05')
        print(' 6. Salir')

        opcion = int(input('  --- ¿Cuál opcion?: '))

        if (opcion == 1):
            Horas()

        elif (opcion == 2):
            Nombre()

        elif (opcion == 3):
            Numero()

        elif (opcion == 4):
            Dato()

        elif (opcion == 5):
            Letras()

        elif (opcion == 6):
            print()


opcion()


def Horas():
    Horas = float(input("Ingresar horas de trabajo:"))
    print("")
    PagoSalario = float(input("Ingresa el pago por hora:"))
    print("")
    Redencion = Horas * PagoSalario
    print("")
    PagoSalarioFinal = Redencion
    print("El pago de trabajo realizado es de :", PagoSalarioFinal)


print("")


def Nombre():
    Nombre = input("¿Cual es tu nombre? ")
    print("Bienvenido a la UIA", Nombre.upper())
    print("Bienvenido a la UIA", Nombre.lower())
    print("Bienvenido a la UIA", Nombre.format())


def Numero():
    Numero = int(input("Digite un numero Entero: "))
    if (Numero <= 10):
        Digito = Numero**2
        print(Digito)
    elif (Numero <= 20):
        Digito = Numero**4
        print(Digito)
    elif (Numero <= 30):
        Digito = Numero**6
        print(Digito)
    elif (Numero <= 40):
        Digito = Numero**8
        print(Digito)
    elif (Numero <= 50):
        Digito = Numero**10
        print(Digito)
    else:
        print(0)


def Dato():
    Dato = int(input("Identificar Número Primo:"))
    for n in range(2, int(Dato/2)):
        if (Dato % n) == 0:
            return print("No un número Primo")
    return print("Es un número Primo")


def Letras():
    Letras = input("Ingrese una cadena de texto")
    imprimir = Letras.count("a")
    print("La cantidad de letras A que existen en la Cadena de texto:", imprimir)

