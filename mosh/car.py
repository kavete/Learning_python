
started = False
# stopped = True
while True:
    user_status = input('> ').lower()
    if user_status == "start":
        if started == False:
            print("Car started... ready to go")
            started = True
        else:
            print("Car already started")
    elif user_status == "stop":
        if started == True:
            print("Car stopped")
            # stopped = True
        # elif started == False:
        #     print("Start the car first")
        else:
            print("Car already stopped")
    elif user_status == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit the game ")
    elif user_status == "quit":
        break
    else:
        print("Sorry I do not understand")