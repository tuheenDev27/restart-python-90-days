currect_pin = 7894
attempts = 3
pin = int(input("Enter your pin: "))
while attempts > 0:
    if pin == currect_pin:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Access denied")
        else:
            print("Incorrect pin. Try again.")
            pin = int(input("Enter your pin: "))
