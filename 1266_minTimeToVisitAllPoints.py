'''
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
'''
'''#1: A normal way to fix this issue'''
def minTimeToVisitAllPoints(points):
    times = 0
    if (len(points) == 1):
        return times

    x_cur_pos, y_cur_pos = points[0][0], points[0][1]

    for i in range(1, len(points)):
        xi_tmp, yi_tmp = abs(points[i][0]-x_cur_pos), abs(points[i][1]-y_cur_pos)
        if (xi_tmp == 0) and (yi_tmp != 0):
            times += yi_tmp
        elif (yi_tmp == 0) and (xi_tmp != 0):
            times += xi_tmp
        elif (xi_tmp == yi_tmp):
            times += xi_tmp
        else:
            if (xi_tmp < yi_tmp):
                times += xi_tmp
                if (y_cur_pos>points[i][1]):
                    times += abs(points[i][1]-(y_cur_pos-xi_tmp))
                else:
                    times += abs(points[i][1]-(y_cur_pos+xi_tmp))
            else:
                times += yi_tmp
                if (x_cur_pos>points[i][0]):
                    times += abs(points[i][0]-(x_cur_pos-yi_tmp))
                else:
                    times += abs(points[i][0]-(x_cur_pos+yi_tmp))

        x_cur_pos, y_cur_pos = points[i][0], points[i][1]

    return times

'''#2: 每次移动最近的距离，就是两个点横、纵坐标差值的最大值'''
def minTimeToVisitAllPoints2(points):
    p_start, times = points[0], 0

    for point in points[1:]:
        p_x, p_y = abs(point[0] - p_start[0]), abs(point[1] - p_start[1])
        times += max(p_x, p_y)
        p_start = point

    return times

#times1 = 49088
points1 = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]

points2 = [[1,1],[3,4],[-1,0]]  #7
points3 = [[3,2],[-2,2]]  #5
points4 = [[2,3],[-4,-7]]
points5 = [[431,91],[838,-127]]  #407
print(minTimeToVisitAllPoints2(points1))
