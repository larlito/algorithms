def factorial(n: int):
    result = 1
    if n < 0:
        raise ValueError
    for i in range(2,n+1,1):
        result = result * i

    return result




def fibonacci(n: int):
    array = []
    if n < 0:
        raise ValueError
    for i in range(0,n+1,1):
        array.append(i)

    return array





def count_ones(n: int):
    if not isinstance(n,int):raise TypeError

    if n > 10:
        return n % 10
    else:
        return 0




def pallindrome(n: int):
    array = []
    reverse_array = []
    if not isinstance(n,int): raise TypeError

    if n < 0:
        raise ValueError
    while n != 0:
        number = n % 10
        array.append(number)
        n = n // 10

    for i in range(len(array)-1,0-1,-1):
        reverse_array.append(array[i])

    if array == reverse_array:
        return True
    else:
        return False







