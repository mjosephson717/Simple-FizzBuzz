#Test File

from FizzBuzz import fizzBuzz 

test_1_solution = ['1', '2', 'Fizz']
test_2_solution = ['1', '2', 'Fizz', '4', 'Buzz']
test_3_solution = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
test_4_solution = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22']
#Test 1

test_1 = (fizzBuzz(3))
test_2 = (fizzBuzz(5))
test_3 = (fizzBuzz(15))
test_4 = (fizzBuzz(22))


if test_1 == test_1_solution:
    print('Test 1 Passed')
else:
    print('Test 1 Failed')
    
if test_2 == test_2_solution:
    print('Test 2 Passed')
else:
    print('Test 2 Failed')

if test_3 == test_3_solution:
    print('Test 3 Passed')
else:
    print('Test 3 Failed')  

if test_4 == test_4_solution:
    print('Test 4 Passed')
else:
    print('Test 4 Failed')    