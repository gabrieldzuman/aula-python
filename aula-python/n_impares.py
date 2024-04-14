def imprimir_impares(n):
    contador = 0
    numero = 1
    while contador < n:
        if numero % 2 != 0:
            print(numero, end=" ")
            contador += 1
        numero += 1

def main():
    n = int(input("Digite o valor de n: "))
    imprimir_impares(n)

if __name__ == "__main__":
    main()
