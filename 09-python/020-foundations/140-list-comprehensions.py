numbers = []

for i in range(5):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(5)]
print(numbers)

even_numbers = [i for i in range(5) if i % 2 == 0]
print(even_numbers)
