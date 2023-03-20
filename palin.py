def palindrome(someList):
    status = True
    if len(someList) <= 0:
        return False;
    else:
        for x in range(int(len(someList)/2)):
            if someList[x] != someList[len(someList)-x-1]:
                status = False
        return status
