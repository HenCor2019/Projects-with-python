# 0 1 2 3 4 5 6 7  8  9  10 11
# 0 1 1 2 3 5 8 13 21 34 55 89 
# Fibonacci iterative version

def Fibonacci_Iterative(n=0) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    before = 0
    after = 1
    current = 0
    counter = 0

    while counter < n-1 :
        current = before + after
        before = after
        after = current
        counter += 1

    return current

#Fibonacci test 1
test1 = Fibonacci_Iterative(6)
print(test1)

#Fibonacci recursive  
def Fibonacci_Recursive(n) :
    if n==0 :
        return 0
    
    if n == 1 :
        return 1
    
    return Fibonacci_Recursive(n-1) + Fibonacci_Recursive(n-2)

test2 = Fibonacci_Recursive(6)
print(test2)



