#The sum of even numbers in the list

import unittest

def sum_of_even_numbers(numbers_list):
    sum_of_evens = 0

    for number in numbers_list:
        if isinstance(number, int) and number % 2 == 0:
            sum_of_evens += number
    return sum_of_evens
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class TestEvens(unittest.TestCase):
    def test_empty_list(self):
        actual_result = sum_of_even_numbers([])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_only_even_list(self):
        actual_result = sum_of_even_numbers([2, 4, 6, 8, 10])
        expected_result = 30
        self.assertEqual(expected_result, actual_result)

    def test_only_odd_list(self):
        actual_result = sum_of_even_numbers([1, 3, 5, 7, 9])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_mix_list(self):
        actual_result = sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected_result = 30
        self.assertEqual(expected_result, actual_result)

    def test_list_with_0(self):
        actual_result = sum_of_even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected_result = 20
        self.assertEqual(expected_result, actual_result)

    def test_negative_number_list(self):
        actual_result = sum_of_even_numbers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
        expected_result = -30
        self.assertEqual(expected_result, actual_result)

    def test_mix_number_letters_list(self):
        actual_result = sum_of_even_numbers([0, 1, 'f', True, None, 4, 5, 6, '7', '8', 9, 10.5])
        expected_result = 10
        self.assertEqual(expected_result, actual_result)

    def test_float_number_list(self):
        actual_result = sum_of_even_numbers([0.1, 0.2, 0.4, 0.5, 0.6, 10.0])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)
if __name__ == '__main__':
    unittest.main()

#The average number
def calculate_average(numbers):
    numbers = [n for n in numbers if n != 0]
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5, 0, 0, 0]
result = sum(numbers) / len(numbers)

class TestAverage(unittest.TestCase):

    def test_positive_average(self):
        actual_result = calculate_average(numbers)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)

    def test_empty_average_list(self):
        actual_result = calculate_average([])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_only_zero(self):
        actual_result = calculate_average([0, 0, 0, 0])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_negative_numbers(self):
        actual_result = calculate_average([-1, -3, -5])
        expected_result = -3
        self.assertEqual(expected_result, actual_result)

    def test_one_number(self):
        actual_result = calculate_average([100])
        expected_result = 100
        self.assertEqual(expected_result, actual_result)

    def test_one_zero(self):
        actual_result = calculate_average([0])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_float_numbers(self):
        actual_result = calculate_average([1.5, 2.5, 3.5])
        expected_result = 2.5
        self.assertEqual(expected_result, actual_result)

    def test_mix_numbers(self):
        actual_result = calculate_average([1.5, 2, 3.5, 0, 4])
        expected_result = 2.75
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()

# Cars selection
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


class TestCars(unittest.TestCase):
    def test_absent_search_criteria(self):
        search_criteria = (2024, 1.6, 36000)
        actual_result = filter_and_sort_cars(car_data, search_criteria)
        expected_result = []
        self.assertEqual(expected_result [:5], actual_result)

    def test_absent_car_data(self):
        car_data = {'VAZ': ('silver', 1990, 1.8, 'sedan', 500)}
        actual_result = filter_and_sort_cars(car_data, search_criteria)
        expected_result = []
        self.assertEqual(expected_result[:5], actual_result)

    def test_positive_search_data(self):
        car_data = {'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000)}
        search_criteria = (2020, 3.6, 45000)
        actual_result = filter_and_sort_cars(car_data, search_criteria)
        expected_result = [('Dodge Ram', ('white', 2020, 3.6, 'pickup', 45000))]
        self.assertEqual(expected_result[:5], actual_result)
