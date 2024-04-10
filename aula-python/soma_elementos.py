def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

# Teste da função
lista1 = [1, 2, 3, 4, 5]
print(soma_elementos(lista1))  # Saída esperada: 15

lista2 = [-1, 0, 1]
print(soma_elementos(lista2))  # Saída esperada: 0
