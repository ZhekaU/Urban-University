immutable_var=1,True,'Мама'
print(immutable_var)
#immutable_var[1]=False # Закоментил, чтобы не ругался 
print(immutable_var) # Кортеж не работает с обращением на конкретный элемент и не изменяет его
mutable_list=([1,True,'Мама'],2024)
mutable_list[0][0]=2020
print(mutable_list)