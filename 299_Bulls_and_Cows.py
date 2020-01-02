"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is.
Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows").
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

'''#1: 匹配的数字（bulls）要移除，不匹配的数字也需要移除，这样才能去重。'''
def getHint1(secret, guess):
    bulls_count, cows_count, i = 0, 0, 0
    bulls_idx = []

    ll = len(guess)

    while (ll != 0):
        if (guess[i] == secret[i]):
            bulls_count += 1
            bulls_idx.append(i)
        i += 1
        ll -= 1

    secret_list = list(secret)
    guess_list = list(guess)

    for i in range(len(bulls_idx)):
        bulls_idx[i] -= i
        secret_list.pop(bulls_idx[i])
        guess_list.pop(bulls_idx[i])

    for item in (guess_list):
        if (item in secret_list):
            cows_count += 1
            secret_list.remove(item)  #去重处理

    return str(bulls_count)+'A'+str(cows_count)+'B'

'''#2: 肖哥的版本，学习思路和处理方法'''
def getHint2(secret, guess):
    bulls_count, cows_count = 0, 0
    non_bulls_secret_list, non_bulls_guess_list = [], []

    #下面这段写的很精妙
    for i in range(len(secret)):
        if (secret[i] == guess[i]):  #对应相等则计数为bulls
            bulls_count += 1
        else:  #对应不等，则将这些元素分别放进list中
            non_bulls_secret_list.append(secret[i])
            non_bulls_guess_list.append(guess[i])

    print(non_bulls_guess_list,non_bulls_secret_list)
    #处理list中cows的部分，注意要做去重处理
    for item in set(non_bulls_guess_list):
        cows_count += min(non_bulls_secret_list.count(item), non_bulls_guess_list.count(item))

    return str(bulls_count)+'A'+str(cows_count)+'B'


secret, guess = "1807", "7810"  #"1A3B"
secret1, guess1 = "1123", "0111"  #1A1B
secret2, guess2 = "1122", "2211"  #"0A4B"
secret3, guess3 = "11", "11"  #"2A0B"
secret4, guess4 = "1122", "0001"  #"0A1B"
print(getHint2(secret, guess))