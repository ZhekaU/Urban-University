def get_multiplied_digits(number):
    str_number = str(number) #Преобразовываем число в строку
    first = (int(str_number[0])) # Отделяем первую цифру
    if len(str_number) > 1:  # Перебираем длину строки
        return first * get_multiplied_digits(int(str_number[1:])) # Вызываем функцию для оставшихся чисел
    else:
        return first # Возвращаем первую цифру если она единственная 


result = get_multiplied_digits(40203)
print(result)
