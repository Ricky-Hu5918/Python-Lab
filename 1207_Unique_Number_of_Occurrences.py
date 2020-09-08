'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation:The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length<= 1000
-1000 <= arr[i] <= 1000
'''

class Solution:
    def uniqueOccurrences1(self, arr) -> bool:
        occurrences = dict()

        for each in arr:
            occurrences[each] = occurrences.get(each, 0) + 1

        return len(occurrences.values()) == len(set(occurrences.values()))

    def uniqueOccurrences2(self, arr) -> bool:
        cn = []
        arrSet = list(set(arr))

        for i in range(len(arrSet)):
            cn.append(arr.count(arrSet[i]))

        return  (len(set(cn)) == len(cn))

test = Solution()
arr = [1,2,3,2,3,3,]
print(test.uniqueOccurrences1(arr), test.uniqueOccurrences2(arr))
