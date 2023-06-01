def find_max_number_index(arr):
    if len(arr) == 0:
        return None

    max_num = arr[0]
    max_number_index = 0

    for index, num in enumerate(arr):
        if num > max_num:
            max_num = num
            max_number_index = index

    return max_number_index

def count_trailing_zeros(n):
    if n == 0:
        return None
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i

    str_factorial = str(factorial_result)
    count = 0
    for i in reversed(range(len(str_factorial))):
        if str_factorial[i] !="0" : 
            break
        else: 
            count+=1
        
    return count

if __name__ == "__main__":
    #input
    array = [4, 9, 2, 7, 5]
    max_index = find_max_number_index(array)
    print("The index of the maximum number is:", max_index)
    #input
    n= 20
    tail_zero = count_trailing_zeros(n)
    print("N of zeros in tail of ", n, "factorial is ",  tail_zero)
