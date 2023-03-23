while True:
    x = eval(input("digite x: "))
    y = eval(input("digite y: "))
    if -10 <= x <= 10 and -10 <= y <= 10:
        if -8 <= x <= 8 and -8 <= y <= 8:
            print("está dentro!")
            break
        else:
            print("Fora!")

