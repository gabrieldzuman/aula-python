# Solicita um número inteiro ao usuário
numero = input("Digite um número inteiro: ")

# Inicializa a soma dos dígitos
soma = 0

# Intera sobre cada dígito no número
for digito in numero:
    # Converte o dígito para inteiro e adiciona à soma
    soma += int(digito)

# Imprime a soma dos dígitos
print("A soma dos dígitos é:", soma)
