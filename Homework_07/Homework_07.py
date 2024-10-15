# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(a, b):
    return a + b

result = sum_numbers(5, 5)
print(f'The sum of two numbers is {result}')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
result = sum(numbers) / len(numbers)
print(int(result))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_text(words):
    return words[::-1]
text = 'My name is...'
reverse_text = reverse_text(text)
print(reverse_text)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_words(w):
    return max(w, key=len)
words = ['cat', 'book', 'phone', 'go']
longest_w = longest_words(words)
print(longest_w)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
#Find the word that contains "h"
def word_list():
    while True:
        word_h = input("Enter a word: ")
        if 'h' not in word_h:
            print('This word doesn\'t contain \'h\'. Please enter another word.')
        else:
            print('Thank you! The word contains \'h\'.')
            return word_h.lower()

result = word_list()

# task 8
#Distribute the list data by the data type
def data_type_list(list_1):
    list_str = []
    list_int = []
    list_bool = []

    for i in list_1:
        if type(i) == str:
            list_str.append(i)
        elif type(i) == int:
            list_int.append(i)
        elif type(i) == bool:
            list_bool.append(i)

    return list_str, list_int, list_bool

list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

strings, integers, booleans = data_type_list(list_1)

print("Strings:", strings)
print("Integers:", integers)
print("Booleans:", booleans)

# task 9
#The sum of even numbers in the list
def sum_of_even_numbers(numbers_list):
    sum_of_evens = 0

    for number in numbers_list:
        if number % 2 == 0:
            sum_of_evens += number
    return sum_of_evens

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'The sum of even numbers: {sum_of_even_numbers(numbers_list)}')

# task 10
#Select the car by search criteria

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

def filter_and_sort_cars(car_data, search_criteria):
    selected_cars = []

    for car_name, car_parameters in car_data.items():
        car_year = car_parameters[1]
        car_engine = car_parameters[2]
        car_price = car_parameters[4]

        if car_year >= search_criteria[0] and car_engine >= search_criteria[1] and car_price <= search_criteria[2]:
            selected_cars.append((car_name, car_parameters))

    sorted_cars = sorted(selected_cars, key=lambda x: x[1][4])

    return sorted_cars[:5]

filtered_cars = filter_and_sort_cars(car_data, search_criteria)
for car in filtered_cars:
    print(f"{car[0]}: {car[1]}")
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""