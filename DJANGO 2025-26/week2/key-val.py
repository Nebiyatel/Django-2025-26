grades = {"John": "A", "Sara": "B", "Musa": "A"}

flipped = {}

for key, value in grades.items():
    if value not in flipped:
        flipped[value] = []        
    flipped[value].append(key)     

print(flipped)
