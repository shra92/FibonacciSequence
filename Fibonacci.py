def getFibonacci(input):
    input = int(input)
    if  input > 0:
        first = 0
        second = 1
        sum = first + second;  #0,1,1,2,3,5,8,13
        count = 1
        print(first); print(second)
       
        while count < input-2:
            count = count+1
            first = second
            second = sum
            sum = first + second
            print(sum)
            
    
number = input("Enter the number of Fibonacci series needed ")
getFibonacci(number)