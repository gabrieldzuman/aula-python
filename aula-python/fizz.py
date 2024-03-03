def fizz_buzz(numero):
    if numero % 3 == 0:
        print("Fizz")
    else:
        print(numero)

numero = int(input("Digite um número inteiro: "))
fizz_buzz(numero)
