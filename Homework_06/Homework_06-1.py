animals_list = []
for animal_item in range(13):
    animal = input(f'Enter animal {animal_item + 1}: ')
    animals_list.append(animal.strip())
print(f'The list of animals: {animals_list}')
unique_animals = set(animals_list)
print(f'Unique animals: {unique_animals}')
if len(unique_animals) == len(animals_list):
    print(True)
else:
    print(False)

#Sheep, Fox, Cat, Dog, Fish, Rabbit, Turtle, Snake, Rat, Chinchilla, Bird