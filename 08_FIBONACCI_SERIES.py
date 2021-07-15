# Two ways to show fibonacci series-->
import time

# Method 1:
# This method has no boundation, but the condition depends on your computer ram.
def fiboIter(n):
    prevNum = 0
    currentNum = 1
    for i in range(1, n):
        prevprevNum= prevNum
        prevNum = currentNum
        currentNum = prevNum +prevprevNum
    return currentNum

# Method 2:
# This method has its limits which we can't surpass.
# This is really a slow thing on comparison to iterative approach
def fiboRecur(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)
if __name__ == "__main__":
    num = int(input("enter your number: "))
    init =time.time()
    print(f"Using recursions value of fib({num}) is {fiboRecur(num)}")
    print(f"Using iterative value of fib({num}) is {fiboIter(num)}")
    print (f"It took {time.time()- init} seconds")