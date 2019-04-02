"""
    This is a demo of a math puzzle that Gerald from the 
meat counter at the WholeFoods I work at gave me. 
    The problem involves a sequence of lockers whose doors are open (or closed).
There are an equal number of curious students as there are lockers. The first
student goes and closes every locker door (redundant). The second goes and
changes the state of every second door (skipping the first, third...). In
general, the nth kid changes the state of every nth door.
    The question is which doors remain closed (or the anti-initial state)
after all students go through and why. The answer is that only the 
lockers whose number is a square are the ones closed.
"""


def initializeList(n):
    theList = [0 for i in range(n)]
    return theList

def printList(aList):
    for i in range(len(aList)):
        print("Item " + str(i+1) + ": \t" + str(aList[i]))
    print("\n")
    return
        

def changeState(aList, idx):
    if aList[idx] == 1:
        aList[idx] = 0
    else:
        aList[idx] = 1
    return


def checkForSquares(aList):
    allGood = True
    for i in range(len(aList)):
        if ((i+1)**(1/2))%1 == 0 and aList[i] != 1:
            allGood = False
        if ((i+1)**(1/2))%1 != 0 and aList[i] != 0:
            allGood = False
    return allGood


def runList(aList):
    """
            The way this one works is that for a given sequence of lockers
        'aList,' for each run, or for each student, or for each 1<=x<=n, 
        check to see which whole multiples of x are not greater than n, i.e.
        k*x <= n for k an integer, then keep track of these, k*x 
        in the 'divisors' list (not the best name). Then change the state of
        the elements in the sequence at positions corresponding to those noted
        in the 'divisors' list, i.e., at the k*x positions.
    """

    for x in range(len(aList)):
        divisors = []
        for k in range(0, int(  len(aList)/(x+1) +1  )):
            if k*(x+1) <= len(aList):
                if k*(x+1)-1 >= 0:
                    divisors.append(k*(x+1)-1)

        "Un-comment these to check 'divisors' list"
        #print("Run "+str(x+1))     
        #printList(divisors)

        for idx in divisors:
            changeState(aList, idx)

    return



def main():
    dummyList = initializeList(
            int(input("Input a number bigger than zero but probably "+
                "not too big lol:\n>>> "))
        )
    runList(dummyList)

    if input("See the list at the end? [y/n]\n>>> ") == "y":
        printList(dummyList)

    print(
        checkForSquares(dummyList)
    )
    return
if __name__ == '__main__':
    main()