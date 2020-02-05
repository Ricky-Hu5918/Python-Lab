'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
'''
'''思路：建立两个字符串每个元素的对应关系，如果对应关系出现冲突，则为false'''
'''#1: timeout. 思路：将字符串中每个元素出现的位置放入列表中，如果列表相等，则为true'''
def isIsomorphic(s, t):
    idx_s = [[] for x in range(len(s))]
    idx_t = [[] for x in range(len(t))]

    for i in range(len(s)):
        idx_s[i].append(i)
        idx_t[i].append(i)

        for j in range(i+1, len(s)):
            if (s[i] == s[j]):
                idx_s[i].append(j)
            if (t[i] == t[j]):
                idx_t[i].append(j)

    print(idx_s, idx_t)
    if (idx_s == idx_t):
        return True
    else:
        return False

'''#2: refer to others solution'''
def isIsomorphic1(s, t):
    return [*map(s.index, s)] == [*map(t.index, t)]

'''#3: xk's solution'''
def isIsomorphic2(s, t):
    d = dict()
    print(dict(zip(s,t)))
    for i, j in (zip(s, t)):
        print(i, j, d)
        if i in d:
            if d[i] != j:
                return False
        elif j not in d.values():
            d[i] = j
        else:
            return False

    return True

'''#4: lj's solution'''
def isIsomorphic3(s, t):
    d = dict()

    for i in range(len(s)):
        if s[i] not in d:
            if t[i] not in d.values():
                d[s[i]] = t[i]
            else:
                return False
        else:
            if d[s[i]] != t[i]:
                return False

    return True

s1, t1 = 'paper', 'title'
s2, t2 = 'ab', 'aa'
s3, t3 = 'foo', 'bar'
print(isIsomorphic3(s1, t1))