import random
random_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random_number_1 = random.choice(random_number) # Генерация случайного числа
print (f"Случайное число: {random_number_1}")
pairs = [] #Поиск пар чисел
for i in range(1, random_number_1):
    for j in range(i + 1, random_number_1):
        if random_number_1 % (i + j) == 0:
            pairs.append((i, j))
result = ''
for i, j in pairs:
    result += f"{i}{j}"
print("Пары чисел:")
print(result)
