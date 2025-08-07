names = [input(f"Enter name {i+1}: ") 
         for i in range(5)]

for i in range(len(names)):
    print(f"Index {i}: {names[i]}")
