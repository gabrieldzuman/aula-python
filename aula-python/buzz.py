def fizz_buzz(numero):
    if numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)

numero = int(input("Digite um número inteiro: "))
fizz_buzz(numero)
