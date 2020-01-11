command = ""
started = False
got_help = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car has already started!!!")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("The car has already stopped!!!")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        if  got_help:
            print("Look on your screen and dot press this button anymore!!!")
        else:
            got_help = True
            print("""
start - start the car
stop - stop the car
quit - quit the game""")
    elif command == "quit":
        break
    else:
        print("i don't understand that...")
