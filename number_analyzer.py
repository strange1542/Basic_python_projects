positive_count = 0 
negative_count = 0

positive_total = 0
negative_total = 0

largest = 0
smallest = 0

first_number = True

while True:
    number = int(input("Enter number :"))

    if number == 0:
        print("you have entered zero so you cannot get further")
        break

    if number > 0:
        positive_count += 1
        positive_total += number

    elif number < 0:
        negative_count += 1
        negative_total += number

    if first_number:
        largest = number
        smallest = number
        first_number = False

    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number


print("Positive count :",positive_count)
print("Poositive total :",positive_total)

print("Negative count :",negative_count)
print("Negative total :",negative_total)

print("Largest number :",largest)
print("Smallest number :",smallest)
