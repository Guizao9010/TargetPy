def fibonacci(num):
    if num < 0:
        return False
    
    t1, t2 = 0, 1

    while t1 <= num:
        if t1 == num:
            return True
        t1, t2 = t2, t1 + t2

    return False

valor = int(input("Digite um número: "))

if fibonacci(valor):
    print(f"O número {valor} pertence à sequência de Fibonacci.")
else:
    print(f"O número {valor} não pertence à sequência de Fibonacci.")

