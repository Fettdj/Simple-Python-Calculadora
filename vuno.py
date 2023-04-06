def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("No se puede dividir por cero.")
        return None
    else:
        return a / b

def calculadora():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Selecciona una operación (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == '1':
        print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
    elif operacion == '2':
        print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
    elif operacion == '3':
        print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
    elif operacion == '4':
        resultado = division(num1, num2)
        if resultado is not None:
            print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    calculadora()
