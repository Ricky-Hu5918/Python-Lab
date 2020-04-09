'''
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
'''

def reverseBits1(n):
    ans, pow = 0, 31

    while (n):
        ans += (n &1) << pow
        n >>= 1
        pow -= 1

    return ans

def reverseBits2(n):
    ans, pow = 0, 31

    while (pow >= 0):
        ans <<= 1
        ans += (n & 1)
        n >>= 1
        pow -= 1

    return ans

def reverseBits3(n):
    ans = ''
    while (n > 0): #reverse bits
        ans += str(n & 1)
        n >>= 1

    for i in range(len(ans), 32): #add 0s, making it to 32bits
        ans += '0'

    return int(('0' + 'b' + ans), 2) #add bianry flag 0b


n = 0b00000010100101000001111010011100
print(reverseBits1(n), reverseBits2(n))
print(reverseBits3(n))