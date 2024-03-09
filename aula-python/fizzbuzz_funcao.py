def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero

# Exemplos de execução
print(fizzbuzz(3))    # Saída: 'Fizz'
print(fizzbuzz(5))    # Saída: 'Buzz'
print(fizzbuzz(15))   # Saída: 'FizzBuzz'
print(fizzbuzz(4))    # Saída: 4
