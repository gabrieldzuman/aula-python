# Recebendo os segundos do usuário
segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

# Calculando dias, horas, minutos e segundos
dias = segundos // (24 * 3600)
segundos_rest = segundos % (24 * 3600)
horas = segundos_rest // 3600
segundos_rest %= 3600
minutos = segundos_rest // 60
segundos_rest %= 60

# Imprimindo o resultado formatado
print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos_rest))
