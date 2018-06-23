# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2010 Round 2 - Problem B. World Cup 2010
# https://code.google.com/codejam/contest/635102/dashboard#s=p1&a=1
#
# Time:  O(P * 2^P)
# Space: O(P * 2^P)
#

def world_cup_2010():
    P = input()
    cost = []
    for _ in xrange(P+1):
        cost.extend(map(int, raw_input().strip().split()))
    cost.reverse()

    dp = [[float("inf") for _ in xrange(P+2)] for _ in xrange(2**(P+1)-1)]
    for i in reversed(xrange(2**(P+1)-1)):
        for j in reversed(xrange(P+1)):
            if i >= 2**P-1:
                if j >= P-cost[i]:
                    dp[i][j] = 0
            else:
                dp[i][j] = min(cost[i] + dp[i*2+1][j+1] + dp[i*2+2][j+1],
                               dp[i*2+1][j] + dp[i*2+2][j])
    return dp[0][0]
    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, world_cup_2010())
