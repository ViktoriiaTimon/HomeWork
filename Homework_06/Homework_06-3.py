#Version 1
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list_str = []
list_int = []
list_bool = []
for i in list1:
    if isinstance(i, str):
        list_str.append(i)
    if isinstance(i, int):
        list_int.append(i)
    elif isinstance(i, bool):
        list_int.append(i)
print("Strings:", list_str)
print("Integers:", list_int)
print("Booleans:", list_bool)

#Version 2
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

list_str = []
list_int = []
list_bool = []

for i in list1:
    if type(i) == str:
        list_str.append(i)
    elif type(i) == int:
        list_int.append(i)
    elif type(i) == bool:
        list_bool.append(i)

print("Strings:", list_str)
print("Integers:", list_int)
print("Booleans:", list_bool)