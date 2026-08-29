numbers = []

while True:
    number = int(input("Enter number : "))

    if number == 0:
        break

    numbers.append(number)

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    print("Numbers :",numbers)

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

total = 0

for number in numbers:
    total += number

avg = total/len(numbers)

print("Largest :",largest)
print("Smallest :",smallest)
print("Total :",total)
print("Average :",avg)
