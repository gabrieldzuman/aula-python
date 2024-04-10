def remove_repetidos(lista):
    # Remover elementos repetidos e ordenar a lista
    lista_sem_repeticao = sorted(set(lista))
    return lista_sem_repeticao

# Teste da função
lista1 = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista1))  # Saída esperada: [1, 2, 3, 4]

lista2 = [1, 2, 3, 3, 3, 4]
print(remove_repetidos(lista2))  # Saída esperada: [1, 2, 3, 4]
