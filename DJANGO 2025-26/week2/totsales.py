
sales = []   
total = 0    

try:
    with open("sales.txt", "r") as file:
        for line in file:
            try:
                num = int(line.strip())  
                sales.append(num)         
                total += num              
            except ValueError:
            
                pass

    print("Valid Sales Numbers:", sales)
    print("Total Sales =", total)

except FileNotFoundError:
    print("sales.txt file not found!")
