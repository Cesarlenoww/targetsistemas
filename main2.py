def pertence_fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    
    while a < n:
        a, b = b, a + b
    return a == n

numero = 21  

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")