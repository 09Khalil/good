import random

with open('city.txt', 'r') as file:
    city_list = [line.strip() for line in file]

used_cities = []


import random

with open('City.txt', 'r', encoding='utf-8') as file:
    city_list = [line.strip() for line in file]

used_cities = []

user_registr = input('Введите свой город: ')

if user_registr in used_cities:
        print('Играем') 

print("Добро пожаловать в игру 'Города'! Давайте начнем!")

while True:
        user_city = input("Ваш город: ").strip().capitalize()

        if user_city == 'Выход':
            print("Игра завершена. До свидания!")
            break

        if user_city in used_cities:
            print(f"Город '{user_city}' уже был назван. Попробуйте другой.")
            continue

        if user_city not in city_list:
            print(f"Города '{user_city}' нет в списке или уже был назван. Попробуйте другой.")
            continue

        used_cities.append(user_city)
        city_list.remove(user_city)

        last_letter = user_city[-1].upper()
        valid_cities = [city for city in city_list if city and city[0].upper() == last_letter and city not in used_cities]

        if not valid_cities:
            print("Я больше не могу найти подходящий город. Вы победили!")
            break

        bot_city = random.choice(valid_cities)
        print(f"Мой город: {bot_city}")

        used_cities.append(bot_city)
        city_list.remove(bot_city)

print("Спасибо за игру!")