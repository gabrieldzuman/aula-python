def eh_primo(num):
    """
    Verifica se um número é primo.

    Argumento:
    num (int): O número a ser verificado.

    Retorna:
    bool: True se o número for primo, False caso contrário.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def maior_primo(numero):
    """
    Retorna o maior número primo menor ou igual ao número dado.

    Argumento:
    numero (int): O número dado.

    Retorna:
    int: O maior número primo menor ou igual ao número dado.
    """
    maior_primo_encontrado = None
    for i in range(numero, 1, -1):
        if eh_primo(i):
            maior_primo_encontrado = i
            break
    return maior_primo_encontrado

# Exemplos de execução
print(maior_primo(100))  # Saída: 97
print(maior_primo(7))    # Saída: 7
