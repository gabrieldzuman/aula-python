def verificar_ordem(a, b, c):
    if a < b < c:
        print("crescente")
    else:
        print("não está em ordem crescente")

# Recebendo os três números inteiros como entrada
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Chamando a função para verificar a ordem
verificar_ordem(numero1, numero2, numero3)
