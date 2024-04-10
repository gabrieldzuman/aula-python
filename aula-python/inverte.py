def main():
    numeros = []

    # Solicita números até que 0 seja inserido
    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        numeros.append(numero)

    # Imprime os números na ordem inversa
    print("Sequência inversa:")
    for num in reversed(numeros):
        print(num, end="")

if __name__ == "__main__":
    main()
