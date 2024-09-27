#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go" said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that" said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azovske_sea = 37800
total_area = black_sea + azovske_sea
print(f'Чорне і Азовське моря разом займають {total_area} км²')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
goods_1_and_2 = 250449
goods_2_and_3 = 222950

warehouse_3 = total_goods - goods_1_and_2
warehouse_1 = total_goods - goods_2_and_3
warehouse_2 = total_goods - (warehouse_1 + warehouse_3)
check = warehouse_3 + warehouse_2 + warehouse_1


print(f"Товари на складі 1: {warehouse_1}")
print(f"Товари на складі 2: {warehouse_2}")
print(f"Товари на складі 3: {warehouse_3}")
print(check)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_monthly = 1179
payment_duration = 18

computer_cost = payment_monthly * payment_duration

print(f"Вартість комп'ютера складає {computer_cost} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
print(a)

b = 9907 % 9
print(b)

c = 2789 % 5
print(c)

d = 7248 % 6
print(d)

e = 7128 % 5
print(e)

f = 19224 % 9
print(f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 274
midl_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

total_money = (big_pizza_price * 4) + (midl_pizza_price * 2) + (juice_price * 4) + cake_price + (water_price * 3)
print(f'Вартість замовлення {total_money} гривен')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo = 232
photo_per_page = 8
pages = int(total_photo / photo_per_page)
print(f'Всього знадобиться {pages} сторінок')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
gasoline_consumption = 9
tank_capacity = 48
total_gasoline = distance / 100 * gasoline_consumption
print(f'{total_gasoline} літрів палива')
needed_refules = int(total_gasoline / tank_capacity)
print(f'{needed_refules} заправок')

