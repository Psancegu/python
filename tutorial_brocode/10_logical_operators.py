temp = int(input("What is the temperature outside?: "))

if 0 < temp < 30: #equivalent to and
    print("The temperature is good today")
    print("Touch some grass")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
    print("Don't touch grass")


# not = "!="