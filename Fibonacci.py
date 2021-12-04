def getFibonacci(input):
    result = []
    if type(input) != int:
        print("Please enter a number greater than 0")
    elif  input > 0:
        first = 0
        second = 1
        sum = first + second;  #0,1,1,2,3,5,8,13
        count = 1
        result.append(first)
        result.append(second)
        result.append(sum)
        while count < input-2:
            count = count+1
            first = second
            second = sum
            sum = first + second
            result.append(sum)

        print(result)
        return result
    else: print("Number must be greater than 0")       

finalresult = getFibonacci(8)