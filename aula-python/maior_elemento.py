def maior_elemento(lista):
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia
    else:
        maior = lista[0]  # Assume o primeiro elemento como o maior
        for elemento in lista:
            if elemento > maior:
                maior = elemento
        return maior

# Teste da função
lista1 = [1, 5, 3, 9, 2]
print(maior_elemento(lista1))  # Saída esperada: 9

lista2 = [-1, -5, -3, -9, -2]
print(maior_elemento(lista2))  # Saída esperada: -1

lista3 = []
print(maior_elemento(lista3))  # Saída esperada: None (lista vazia)
