import os
import random

filename = "counter.txt"
start_numbers = ["400", "410", "730", "900"]  # Country designations: 1.Germany, 2.Sweden, 3.Austria, 4. Germany
middle_numbers = ["8844", "0723", "0456"]  # Company numbers
end_number = ["5678"] # Article number

repeat_count = int(input("How many codes should be created? "))

for _ in range(repeat_count):
    random_start_number = random.choice(start_numbers)
    random_middle_number = random.choice(middle_numbers)
    random_end_number = random.choice(end_number)

    print(random_start_number , random_middle_number , random_end_number)
