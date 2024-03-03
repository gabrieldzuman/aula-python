# Solicita o valor de "n" ao usuário
n = int(input("Digite o valor de n: "))

# Inicializa uma variável para contar os números ímpares
count = 0

# Inicializa uma variável para armazenar o número atual
num = 1

# Imprime os "n" primeiros números ímpares
print("Os", n, "primeiros números ímpares são:")
while count < n:
    if num % 2 != 0:
        print(num)
        count += 1
    num += 1
