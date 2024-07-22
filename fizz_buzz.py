chosen_number = int(input("choose a number:"))

for number in range(1, chosen_number + 1):
    if(number % 3 == 0 and number % 5 == 0):
        print("fizz buzz")
    elif(number % 3 == 0):
        print("fizz")
    elif(number % 5 == 0):
        print("buzz")
    else:
        print(number)