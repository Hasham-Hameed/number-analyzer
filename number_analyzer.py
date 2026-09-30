number_of_numbers = int(input("How many numbers you want to enter: "))

numbers = []
for i in range(number_of_numbers):
    number = int(input("Enter the number: "))
    numbers.append(number)

def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
calculated_total = calculate_total(numbers)

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average
calculated_average = calculate_average(numbers)

def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
found_largest = largest_number(numbers)

def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
found_smallest = smallest_number(numbers)

def positive_numbers(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count
found_positive = positive_numbers(numbers)

def negative_numbers(numbers):
    count = 0 
    for number in numbers:
        if number < 0:
            count += 1
    return count
found_negative = negative_numbers(numbers)

def number_of_zeros(numbers):
    count = 0
    for number in numbers:
        if number == 0:
            count += 1
    return count
found_number_of_zeros = number_of_zeros(numbers)

def even_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count
found_even_numbers = even_numbers(numbers)

def odd_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    return count
found_odd_numbers = odd_numbers(numbers)

print(f"Total: {calculated_total}")
print(f"Average: {calculated_average}")
print(f"Largest number: {found_largest}")
print(f"Smallest number: {found_smallest}")
print(f"Number of positive integers: {found_positive}")
print(f"Number of negative integers: {found_negative}")
print(f"Number of zeros: {found_number_of_zeros}")
print(f"Number of even numbers: {found_even_numbers}")
print(f"Number of odd numbers: {found_odd_numbers}")