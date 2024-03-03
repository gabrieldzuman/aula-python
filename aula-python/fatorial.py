def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Solicita o valor de "n" ao usuário
n = int(input("Digite o valor de n: "))

# Calcula o fatorial de "n"
resultado = fatorial(n)

# Imprime o resultado
print(f"{n}! =", resultado)
