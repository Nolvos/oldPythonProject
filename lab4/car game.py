command = ""
start = False
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start" and not start:
        print("Car started ..")
        start = True
    elif command.lower() == "start" and start:
        print("the car is already working")
    elif command.lower() == "stop" and start:
        print("Car stopped ..")
        start = False
    elif command.lower() == "stop" and not start:
        print("the car already stopped")
    elif command.lower() == "help":
        print(""
              "start: to start the car"
              "stop: to stop the car"
              "quit: to quit"
              "")
    elif command == "quit":
        break
    else:
        print("Sorry !!I don't understand what you need")