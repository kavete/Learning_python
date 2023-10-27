is_started = False
is_stopped = True

while True:
    command = input('> ').lower()
    if command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit the game ")
    elif command == "quit":
        break
    elif command == "start":
        if is_started:
            print("Car already started")
        else:
            print("Car started")
            is_started = True
            is_stopped = False
    elif command == "stop":
        if is_stopped:
            print("Car already stopped")
        else:
            print("Car stopped")
            is_stopped = True
            is_started = False
    else:
        print("I do no understand")
