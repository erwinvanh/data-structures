# python2

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
# Contains the following info :
# 1 : Has parent been merged
# 2 : Number of rows in merged set
# 3 : Merged to physical table x
parentMapping = [["N", -1, -1]] * n
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def printInfo():
    print "Rank " , rank
    print "Lines ", lines
    print "Parents ", parent
    print "ParentMapping ", parentMapping

def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        #print "Destination ", destination, " and ", source, " are already in same set"
        return False

    if parentMapping[realSource][0] == "J":
        #print "From parentMapping"
        sourceCount = parentMapping[realSource][1]
        sourceContainer = parentMapping[realSource][2]
    else:
        #print "from lines"
        sourceCount = lines[realSource]
        sourceContainer = realSource

    #print "Sourcecount ", sourceCount

    if parentMapping[realDestination][0] == "J":
        #print "From parentMapping"
        destinationCount = parentMapping[realDestination][1]
        destinationContainer = parentMapping[realDestination][2]
    else:
        #print "from lines"
        destinationCount = lines[realDestination]
        destinationContainer = realDestination

    #print "destinationCount ", destinationCount

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        print "Using destination as parent"
    else:
        print "Using source as parent"
        parent[realDestination] = realSource
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1

    #print "Merging ", realSource , "  to " , realDestination
    total = sourceCount + destinationCount
    lines[destinationContainer] = total
    parentMapping[getParent(realDestination)] = [ "J" , total, destinationContainer]
    lines[sourceContainer] = 0

    if total > ans:
        ans = total

    return True

printInfo()
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    #printInfo()
    print ans

printInfo()
