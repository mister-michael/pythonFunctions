def chickenMonkey(tacos):
    for number in tacos:
        if number % 5 == 0:
            print("Chicken")
            continue
        if number % 7 == 0:
            print("Monkey")
            continue
        else:
            print(number)

chickenMonkey(range(0,100))