"""
Given an array of integers, return the indices of the two numbers that add up to a given target.
"""
from itertools import combinations

testCases = [
    ([1,3,7,9,2], 11, [3,4]),
]

def subsets(arr: set, num: int) -> list:
   subsets = []
   # This returns all subsets
   # [subsets.extend(list(combinations(arr,n))) for n in range(len(arr))]
   
   # This returns only subsets that have two numbers
   subsets.extend(list(combinations(arr,num)))
   return subsets 


def solution(array, total):
    # return an array
    answer = []
    
    combos = subsets(set(array), 2)
    for combo in combos:
        guess = sum(combo)
        if guess == total:
            break

    for num in combo:
        index = array.index(num)
        answer.append(index)

    answer.sort()
    print(f" answer is {answer}")
    return answer


for index, testCase in enumerate(testCases):
    answer = solution(testCase[0], testCase[1])
    print(f" answer is {answer}")
    if set(answer) == set(testCase[2]):
        print('Correct')
    else:
        print('Not Correct')

