def n_primos(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

# Exemplos de uso
print(n_primos(2))   # Saída: 1 (o único primo entre 2 e 2 é 2)
print(n_primos(4))   # Saída: 2 (os primos entre 2 e 4 são 2 e 3)
print(n_primos(121)) # Saída: 30 (quantidade de primos entre 2 e 121)
