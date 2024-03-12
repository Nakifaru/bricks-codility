#start from index 0 and index -1 checking if less than 10

def solution(A):
    steps = 0
    for index,value in enumerate(A):
        if(value < 10):
            positions_before = 1
            while positions_before <= index:
                if(A[index - positions_before] > 10 and A[index] < 10):
                    while A[index - positions_before] > 10 and A[index] < 10:
                        A[index - positions_before] -= 1
                        A[index] += 1
                        steps += positions_before
                positions_before += 1
            positions_after = 1
            while positions_after <= len(A) - (index + 1):
                if(A[index + positions_after] > 10 and A[index] < 10):
                    while A[index + positions_after] > 10 and A[index] < 10:
                        A[index + positions_after] -= 1
                        A[index] += 1
                        steps += positions_after
                positions_after += 1
    print(A)
    for x in A:
        if x != 10:
            steps = -1
    print(steps) 
    return steps


solution([7, 15, 10, 8]) #7
solution([11, 10, 8, 12, 8, 10, 11]) #6
solution([7, -14, 10]) #-1
    # [num for num in numbers if num == 10]

