def vogal(caractere):
    """
    Verifica se um caractere é uma vogal.

    Argumento:
    caractere (str): O caractere a ser verificado.

    Retorna:
    bool: True se o caractere for uma vogal, False caso contrário.
    """
    vogais = "aeiouAEIOU"
    return caractere in vogais

# Exemplos de execução
print(vogal("E"))  # Saída: True
print(vogal("b"))  # Saída: False
print(vogal("a"))  # Saída: True
