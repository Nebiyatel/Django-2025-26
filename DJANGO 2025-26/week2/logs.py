
with open("log.txt", "a") as file:   
    file.write("User logged in\n")
with open("log.txt", "r") as file:
    history = file.read()
    print("Log History:")
    print(history)
