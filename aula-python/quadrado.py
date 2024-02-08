# Recebendo o valor do lado do quadrado como entrada de dados
lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))

# Calculando o perímetro do quadrado (4 vezes o lado)
perimetro = 4 * lado

# Calculando a área do quadrado (lado ao quadrado)
area = lado ** 2

# Imprimindo o resultado formatado
print(f"perímetro: {perimetro} - área: {area}")
