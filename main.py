import time
x = input("¿What greeting do you want? ")

while True:
    print(x)
    a = input("Do you want another greeting (Y/n), do you want the time (t) or change the greeting(c)")
    match a:
        case "n" | "N":
            break
        case "t" | "T":
            print("The time is " + time.strftime("%H:%M", time.localtime()))
        case "c" | "C":
            x = input("Insert new greeting: ")

