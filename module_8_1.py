def add_everything_up (a = None,b = None):
    try:
        if a is None:
            a = (input('Введите значение а: '))
        if b is None:
            b = (input('Введите значение b: '))
        a = int(a)
        b = int(b)
        t = a + b
        print(t,'Числа успешно сложенны')

    except ValueError :
        a = str(a)
        b = str(b)
        print(f'В значении присутствует текс : {a + b}')

add_everything_up()

