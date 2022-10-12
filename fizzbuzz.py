for x in range(101):
    if (x%15 == 0):
        print("FizzBuzz")
        continue
    elif (x%5 == 0):
        print("Buzz")
        continue
    elif (x%3 == 0):
        print("Fizz")
        continue
    print(x)
