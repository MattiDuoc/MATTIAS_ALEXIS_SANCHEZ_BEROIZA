investigador_principal = 0
investigador_asistente = 0

cientifico = 0
while cientifico == 0:
    try:
        cientifico = int(input("Ingrese la cantidad de Cientificos que desea registrar:\n"))
    except:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

for cantidad in range(1, cientifico + 1):
    print(f"Ingresando Cientifico {cantidad}")
    Codigo = (input('Ingrese Codigo de Cientifico:\n(Debe de contener 12 caracteres):\n')).lower()
    