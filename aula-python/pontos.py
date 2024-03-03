def calcular_distancia(x1, y1, x2, y2):
    distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distancia

# Recebendo as coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calculando a distância entre os dois pontos
distancia = calcular_distancia(x1, y1, x2, y2)

# Verificando se a distância é maior ou igual a 10 e imprimindo o resultado
if distancia >= 10:
    print("longe")
else:
    print("perto")
