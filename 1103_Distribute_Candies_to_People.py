'''
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
'''

'''#1: 每次从头开始增加的部分为k*num_people, k从0开始计数'''
def distributeCandies(candies, num_people):
    ans = [0 for i in range(num_people)]
    tmp = 0

    idx, k = 0, 0
    while (sum(ans) <= candies):
        ans[idx] += tmp + 1 + idx
        if idx < num_people - 1:
            idx += 1
        else:
            k += 1
            idx, tmp = 0, num_people * k
        # print(ans, idx)

    tmp = ans.copy()
    tmp.pop(idx - 1)
    ans[idx - 1] = candies - sum(tmp)

    return ans

candies0, num_people0 = 25, 3  #[9, 7, 9]
candies1, num_people1 = 26, 3  #[10, 7, 9]
candies2, num_people2 = 30, 3  #[12, 9, 9]
print(distributeCandies(candies1, num_people1))