"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""
'''#1: trust[i] = [a, b], a is people, b is judge. The times that the judge was trusted must be N-1'''
'''Firstly, to calculate the times that b was trusted; Secondly, to find the real judge'''
def findJudge(N, trust):
    if (N==1) and (not trust): return N

    trust_relationships = dict()
    town_judge, town_people = 0, []
    for i in range(1, N+1):
        trust_relationships[i] = 0

    for each in trust:
        town_people.append(each[0])
        trust_relationships[each[1]] += 1  #calculate the times that b was trusted'

    print(trust_relationships)
    for k, v in trust_relationships.items():
        if (v == N-1):
            town_judge = k #find the real judge

    if not town_judge: #no judge exists
        return -1
    else:
        if (town_judge not in town_people):  #The town judge trusts nobody
            return town_judge
        else:
            return -1

N1, trust1 = 3, [[1, 3], [2, 3]]  #3
N2, trust2 = 3, [[1,3],[2,3],[3,1]] #-1
N3, trust3 = 4, [[1,3],[1,4],[2,3],[2,4],[4,3]] #3
N4, trust4 = 4, [[1,3],[1,4],[2,3],[2,4],[4,1]] #-1
N5, trust5 = 4, [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]] #3
print(findJudge(N5, trust5))