def maximo(num1, num2):
    """
    Retorna o maior entre dois números inteiros.

    Argumentos:
    num1 (int): O primeiro número inteiro.
    num2 (int): O segundo número inteiro.

    Retorna:
    int: O maior número entre num1 e num2.
    """
    return num1 if num1 > num2 else num2

# Exemplos de execução
print(maximo(3, 4))  # Saída: 4
print(maximo(0, -1)) # Saída: 0
