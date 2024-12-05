import requests

# 1. Отправка GET-запроса и получение данных
response = requests.get('https://urban-university.ru/')
print(response.status_code)  # Код состояния ответа
print(response.text)       # JSON-ответ от сервера

# 2. Передача параметров в запросе
params = {'userId': 1}
response = requests.get('https://urban-university.ru/', params=params)
print(response.status_code)  # Код состояния ответа
print(response.json())       # JSON-ответ от сервера

# 3. Добавление заголовков в запрос
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://urban-university.ru/', headers=headers)
print(response.status_code)  # Код состояния ответа
print(response.json())       # JSON-ответ от сервера


from PIL import Image

# 1. Открытие изображения
img = Image.open('example.jpg')
img.show()

# 2. Изменение размеров изображения
new_size = (800, 600)  # Новый размер
resized_img = img.resize(new_size)
resized_img.save('resized_example.jpg')

# 3. Преобразование изображения в черно-белый формат
bw_img = img.convert('L')
bw_img.save('bw_example.jpg')


import pandas as pd

# 1. Создание DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'New York']
}
df = pd.DataFrame(data)
print('DataFrame:')
print(df)

# 2. Фильтрация данных: выбрать людей старше 30 лет
filtered_df = df[df['Age'] > 30]
print('\nФильтрация данных (возраст > 30):')
print(filtered_df)

# 3. Агрегация данных: подсчет среднего возраста по городам
grouped_df = df.groupby('City')['Age'].mean()
print('\nАгрегация данных (средний возраст по городам):')
print(grouped_df)
