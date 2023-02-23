def floatToString():
    while True:
        try:
            x = input("input a string that you want to convert to a float ")
            f = float(x)
            print(f)
            return f
            break
        except(ValueError):
            print("please enter a convertable value") 

floatToString()