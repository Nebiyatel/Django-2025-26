total = 0
try:
    with open("numbers.txt", "r") as file:
        for line in file:
            try:
                num = int(line.strip())
                total += num
            except ValueError:
                pass
    print("Sum =", total)
except FileNotFoundError:
    print("File not found!")
