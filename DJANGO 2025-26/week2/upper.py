try:
    with open("message.txt", "r") as file:
        for line in file:
            print(line.strip().upper())
except FileNotFoundError:
    print("File not found!")
