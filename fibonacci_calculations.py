def caching_fibonacci():
    cache = {} # creating a dictionary for Fibonacci calculations
    def fibonacci(n): 
        if n <= 0: # base case: the 0th Fibonacci number is 0
            return 0
        elif n == 1: # base case: the 1st Fibonacci number is 1
            return 1
        elif n in cache: # if value is already in cached, return it
            return cache[n]
        
        # calculating Fibonacci nums, store in the dict(cache) and return them
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # recursion
        return cache[n]
    
    # returning the inner function
    return fibonacci 

fib = caching_fibonacci() # example
print(fib(10)) # output: 55
print(fib(15)) # output: 610
print(fib(20))# output: 6765