def factorial(n):
    if(n<0):
        raise ValueError('not defined')
    elif (n==1 or n==0):
        return 1  
    elif (n>1):
        return n*factorial(n - 1) 
 