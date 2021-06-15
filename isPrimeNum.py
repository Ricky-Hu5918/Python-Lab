# check if a number is a prime number or not
# a prime number is a number that has two distinct factors, 1 and itself
# means it is only divisible by 1 and itself. (1 is not a prime number)

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            print("not a prime number!")
            return False

    print("a prime number!")
    return True


number = int(input("pls enter a number to be checked: "))
print(isPrime(number))
