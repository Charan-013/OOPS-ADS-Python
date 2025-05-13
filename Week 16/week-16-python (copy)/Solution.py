def findNode(ele,d,a):
    min_cost = float("inf")
    cost = 0
    min_Node = a
    if ele in d:
        for node in d[ele]:
            min_Node = node[0]
            if node[1] < min_cost:
                min_cost = node[1]
                min_Node = node[0]
    # print(ele,min_Node,min_cost)
        return min_Node,min_cost



def minCostExchangeNetwork(n,lst,m,mLines):
    if n == 1 and m == 0:
        return 0
    elif m == 0:
        return -1
    d = {}
    for ele in mLines:
        if ele[0] not in d:
            d[ele[0]] = [[ele[1],int(ele[2])]]
        else:
            d[ele[0]].append([ele[1],int(ele[2])])
    # print(d)
    visited = []
    cost = 0
    # for ele in lst:
    #     if ele not in visited:
    #         a,temp = findNode(ele,d)
    #         visited.append(ele)
    #         if a not in visited:
    #             visited.append(a)
    #         cost += temp
    # print(d)
    for i in range(n):
        for j in range(i,n):
            if lst[i] not in visited:
                visited.append(lst[i])
                a,temp = findNode(lst[i],d,lst[j])
                if a not in visited:
                    visited.append(a)
                cost += temp

            

    if len(mLines) < len(lst) and m != 1:
        return -1
    if len(lst) != len(visited):
        return -1
    # print(cost)
    if len(lst) == len(visited) and cost == 0:
        return -1              
    return cost




def main():
    n = int(input())
    lst = list(map(str,input().split()))
    m = int(input())
    mLines = []
    for i in range(m):
        mLines.append(input().split())
    try:
        print(minCostExchangeNetwork(n,lst,m,mLines))
    except TypeError:
        print(0)
main()

def findallPaths(g,s,e,path):
    pass