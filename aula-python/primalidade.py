def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))

if verificar_primo(numero):
    print("primo")
else:
    print("não primo")
