for x in range(101):
    ##multiples of 15
    if (x%15 == 0):
        print("FizzBuzz")
        continue
    #multiples of 5
    elif (x%5 == 0):
        print("Buzz")
        continue
    ##multiples of 3
    elif (x%3 == 0):
        print("Fizz")
        continue
    print(x)
