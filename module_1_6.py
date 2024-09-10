my_dict={'Mazda':'М 142 НК 154','Mitsubishi':'Н 476 ТК 142','Mercedes':'А 847 РВ 124' }
print(my_dict)
print(my_dict['Mazda'])
my_dict['BMW']='Л 888 НМ 144'
print(my_dict)
my_dict.update({'Toyota':'Г 454 ЗХ 104', 'Geely':'В 843 ШП 77'})
print(my_dict)
del my_dict ['Mercedes'] #?

print(my_dict)
my_set={2,4,6,2,2,2,3,3,4,4,4,5,5,56,6,False,False,False,False,True,'Молоко'}
print(my_set)
my_set.add(77)
my_set.discard(2)
print(my_set)