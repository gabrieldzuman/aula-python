def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    else:
        print(numero)

numero = int(input("Digite um número inteiro: "))
fizz_buzz(numero)
