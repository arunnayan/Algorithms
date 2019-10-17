
#o(n2)
# def findSum(lst, sum):
#     for i in range(len(lst)):
#         j = i+1
#         for j in range(len(lst)):
#             if lst[i] + lst[j] == sum:
#                 return [lst[i], lst[j]]
#
#     return []
#



def findSum2(lst, sum):
    lst.sort()
    start = 0
    end = len(lst)-1
    s = 0

    while start < end:
        s = lst[start] + lst[end]
        if s == sum:
            return [lst[start], lst[end]]
        if s > sum:
            end = end -1
        elif s< sum:
            start = start+1


    return []


def findSum3(lst, sum):
    foundValues = {}
    for ele in lst:
        try:
            foundValues[sum-ele]
            return [ele, sum-ele]
        except:
            foundValues[ele] = 0


    return []


print(findSum3([1,21,3,14,5, 60,7,6], 81))