# Recebendo um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Calculando o dígito das dezenas
digito_dezenas = (numero // 10) % 10

# Imprimindo o resultado
print("O dígito das dezenas é", digito_dezenas)
