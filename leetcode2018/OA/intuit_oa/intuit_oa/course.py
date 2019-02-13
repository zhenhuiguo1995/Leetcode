import sys

def findMidPointCourse(pairs):
    array = [0 for _ in range(0, len(pairs))]
    pred = [pairs[i][0] for i in range(0, len(pairs))]
    succ = [pairs[i][1] for i in range(0, len(pairs))]

    def traversal(pred, succ, pairs, array):
        for i in range(0, len(array)):
            if array[i] != 1:
                array(pred.index(succ[i])) = 1
                
    return None

def main():
    pairs = []
    for line in sys.stdin:
        if len(line.strip()) == 0:
            continue

        line = line.rstrip()
        paris.append(line.split(" "))
    
    print(findMidPointCourse(pairs))


main()

"""
input

DataStructure Algorithms

"""