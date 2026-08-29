var1 = int(input())
var2 = int(input())

while True:
    var3 = input("what you want to do (+,-,*,/):")

    if var3 == "+" :
        sum = var1 + var2
        print(sum)
        break

    elif var3 == "-":
        diff = var1 - var2
        print(diff)
        break
    elif var3 == "*":
        multiply = var1 * var2
        print(multiply)
        break
    elif var3 == "/":
        divide = var1 / var2
        print(divide)
        break
    else:
        print("please enter any  four symbols.")


