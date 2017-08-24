def search(aList, target):
    for v in aList:
        if target == v:
            return True
    return False

def searchRecursive(aList, target):
    if len(aList) == 0:
        return False
    if aList[0] == target:
        return True
    return searchRecursive(aList[1:], target)
