#Imports
import grade_average_service
import random
import math
#from grade_average_service import calculate

homework_assigment_grades = {
    'Task 1': 85,
    'Task 2': 93,
    'Task 3': 95
}

grade_average_service.calculate(homework_assigment_grades)
# Other types
# Example
list_random = ['coffe', 'tea', 'water', 'juice']
print(random.choice(list_random))
print(random.randint(1, 10))

square_root = math.sqrt(81)
print(square_root)