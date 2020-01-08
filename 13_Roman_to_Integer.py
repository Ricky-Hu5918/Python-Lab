"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
"""

'''#1: 常规查字典方法，效率不高'''
def romanToInt(s):
    single_numbers_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    double_numbers_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    idx, total_num = 0, 0
    while (idx < len(list(s))):
        try:
            total_num += double_numbers_dict[s[idx] + s[idx + 1]]
            idx += 2
        except:
            total_num += single_numbers_dict[s[idx]]
            idx += 1

    return total_num

'''#2: 把字符串处理成单个、直接可以识别的罗马数字'''
def romanToInt1(s):
    all_numbers_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    double_numbers_list = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

    res, idx = [], 0
    ll = len(list(s))
    while (idx<ll):
        if (idx < ll-1) and (s[idx]+s[idx+1]) in double_numbers_list:
            res.append(s[idx] + s[idx + 1])
            idx += 2
        else:
            res.append(s[idx])
            idx += 1

    '''# return sum(all_numbers_dict[item] for item in res) 下面的代码可以用这一行搞定，简洁但效率极其低下'''
    total_num = 0
    for item in res:
        total_num += all_numbers_dict[item]

    return total_num

'''#3: 方法#1和#2的结合优化版'''
def romanToInt2(s):
    all_numbers_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    double_numbers_list = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

    total_num, idx = 0, 0
    ll = len(list(s))
    while (idx<ll):
        if (idx < ll-1) and (s[idx]+s[idx+1]) in double_numbers_list:
            total_num += all_numbers_dict[s[idx]+s[idx+1]]
            idx += 2
        else:
            total_num += all_numbers_dict[s[idx]]
            idx += 1

    return total_num



s = "LVIII"  #58
s1 = "MCMXCIV" #1994
s3 = "IIIIMIIIC"
print(romanToInt2(s1))