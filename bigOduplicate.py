import random
import timeit
def uniqueCheckFast(aList):
    """
    Return True if aList contains any duplicates. It completes in O(n) time with O(n) space required.
    Individual elements must be hashable
    """

    check = set()
    for v in aList:
        if v in check:
            return True
        check.add(v)
    return False
def uniqueCheckSlow(aList):
    """
    Return True if aList contains any duplicates. Completes in O(n^2) time with no space required.
    """

    for i in range(len(aList) - 1):
        for j in range(i+1, len(aList) - 1):
            if aList[i] ==  aList[j]:
                return True
    return False

print('N\tSlow  \tFast')
for trial in [2**_ for _ in range(1,12)]:
    numbers = [random.random() for _ in range(trial)]
    mSlow = timeit.timeit(stmt='uniqueCheckSlow(numbers)', setup='import random\nfrom __main__ import', number=1000)
    mFast = timeit.timeit(stmt='uniqueCheck(numbers)', setup='import random\nfrom __main__ import', number=1000)
    print('{0:d}\t{1:f}\t{2:f}'.format(trial, mSlow, mFast))
