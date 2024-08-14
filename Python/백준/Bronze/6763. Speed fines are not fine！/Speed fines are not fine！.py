a = - int(input()) + int(input())
if (a < 1):
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is $" + ("500" if a >= 31 else "270" if a >= 21 else "100") + ".")