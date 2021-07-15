i = 0
for i in range(6):
    a = input("\nenter anything to reverse\n: ")
    
    for i in range(len(a)):
        y = a[-(i+1)]
        b = print(y, end="")