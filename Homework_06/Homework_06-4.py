numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_evens = 0
for number in numbers_list:
    if number % 2 == 0:
        sum_of_evens += number
print(f'The sum of even numbers: {sum_of_evens}')