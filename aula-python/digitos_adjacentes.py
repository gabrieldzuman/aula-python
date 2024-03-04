def possui_adjacente_igual(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i + 1]:
            return True
    return False

numero = int(input("Digite um número inteiro: "))

if possui_adjacente_igual(numero):
    print("sim")
else:
    print("não")
