'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
'''

def wordPattern1(pattern, str):
    str_list = str.split(' ')
    if (len(pattern) != len(str_list)):
        return False

    d = {}

    for i in range(len(pattern)):
        if pattern[i] not in d:
            if str_list[i] not in d.values():
                d[pattern[i]] = str_list[i]
            else:
                return False
        else:
            if d[pattern[i]] != str_list[i]:
                return False

    return True

def wordPattern2(pattern, str):
    str_list = str.split(' ')
    if (len(pattern) != len(str_list)):
        return False

    d = {}
    for i, j in zip(pattern, str_list):
        if i in d:
            if d[i] != j:
                return False
        elif j not in d.values():
            d[i] = j
        else:
            return False

    return True

def wordPattern3(pattern, str):
    str_list = str.split(' ')
    if (len(pattern) != len(str_list)):
        return False

    return [*map(pattern.index, pattern)] == [*map(str_list.index, str_list)]

pattern1, str1 = 'abba', "dog cat cat dog"  #true
pattern2, str2 = 'abba', "dog cat cat fish" #false
pattern3, str3 = 'aaaa',"dog cat cat dog"  #false
pattern4, str4 = 'aaa', 'aa aa aa aa' #false
print(wordPattern3(pattern4, str4))
