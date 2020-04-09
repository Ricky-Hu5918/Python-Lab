'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''

'''暴力破解法'''
def readBinaryWatch1(num):
    hours, mins = [], []
    ans, hour_num = [], 0

    while (hour_num <= num):
        for i in range(12):
            if (bin(i).count('1') == hour_num):
                hours.append(str(i) + ':')
        # print('h', hours)

        for i in range(60):
            if (bin(i).count('1') == num - hour_num):
                if i >= 10:
                    mins.append(str(i))
                else:
                    mins.append('0' + str(i))
        # print('m', mins)

        for h in hours:
            for m in mins:
                ans.append(h + m)

        # print(ans)
        hours, mins = [], []
        hour_num += 1

    return ans

print(readBinaryWatch1(2))
