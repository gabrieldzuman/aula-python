def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = soma_digitos(numero)
    print("A soma dos dígitos é:", resultado)

if __name__ == "__main__":
    main()
