first= (input('Введите первое число: '))
second=(input('Введите второе число: '))
third=(input('Введите третье число: '))
if first==second==third:
    print(3)
elif first== second or second==third or third==first:
    print(2)
if first!=second!=third:
    print(0)
