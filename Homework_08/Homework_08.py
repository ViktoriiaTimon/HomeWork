def sum_of_items(s):
    try:
        numbers_list = s.split(',')
        return sum(int(num) for num in numbers_list)
    except ValueError:
        return "Impossible to count!"

data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    result = sum_of_items(item)
    print(f"The item in the list: '{item}' The result: {result}")