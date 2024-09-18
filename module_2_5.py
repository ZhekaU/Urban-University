def get_matrix (n,m,value): # Объявляем функцию get_matrix с параметрами n, m и value
 matrix = [] # Создаем пустой список matrix внутри функции get_matrix
 for mat in range (n): # Внешний цикл для строк n
  matrix_1 = []
  matrix.append(matrix_1) # Добавляем пустой список в список matrix
  for mat in range (m): #Внешний цикл для столбцов m
      matrix_1.append (value) # Пополняем пустой список значениями value
  return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)




