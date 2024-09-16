numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
non_primes = []

for i in numbers: # Перебор чисел в списке
    if i > 1:  # 1 не является простым числом
        is_prime = True
        for j in range(2, i): # Определение начала последовательности
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            non_primes.append(i)

print("Простые числа:", primes)
print("Непростые числа:", non_primes)