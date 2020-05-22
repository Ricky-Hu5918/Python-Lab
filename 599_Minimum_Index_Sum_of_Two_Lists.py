'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:

The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
'''


class Solution:
    def findRestaurant2(self, list1, list2):
        common_dict, res = dict(), []
        for k, v in enumerate(list1):
            if v in list2:
                common_dict[v] = k + list2.index(v)

        for k, v in common_dict.items():
            if v == min(common_dict.values()):
                res.append(k)

        return res

    # 1: normal way, not that good
    def findRestaurant1(self, list1, list2):
        common_list = list(set(list1) & set(list2))
        if len(common_list) == 1: return common_list

        least_index_sum = list1.index(common_list[0]) + list2.index(common_list[0])
        res = [common_list[0]]
        for each in common_list[1:]:
            tmp = list1.index(each) + list2.index(each)
            if tmp < least_index_sum:
                least_index_sum = tmp
                res[0] = each

            if (tmp == least_index_sum) and each not in res:
                res.append(each)

        return res

test = Solution()
list1, list2 = ["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]
print(test.findRestaurant1(list1, list2), test.findRestaurant2(list1, list2))