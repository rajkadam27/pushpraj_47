numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique number list:", unique_numbers)