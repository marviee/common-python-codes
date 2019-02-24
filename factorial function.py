def factorial(n):
    if n==1 or n==0:
        return 1
    elif n>1:
        result= n*factorial(n-1)
        return result
    elif n<0:
        print("Enter a valid number, you can only find factorial of positive numbers")
    else:
        print("Enter a valid number ")
print(factorial(5))        
