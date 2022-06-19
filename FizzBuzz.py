def fizzBuzz(n):
    
    newArray = []
    
    for n in range (1,n+1):
        
        if n % 3 == 0 and n % 5 != 0:
            newArray.append('Fizz')
            
        elif n % 5 == 0 and n % 3 != 0:
            newArray.append('Buzz')
        
        elif n % 3 == 0 and n % 5 == 0:
            newArray.append('FizzBuzz')
            
        else:
            newArray.append(str(n))
            
    return newArray

            
        