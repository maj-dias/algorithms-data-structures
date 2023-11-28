import heapq
from typing import List

def solution_dict(score:List[int]) -> List[str]:
    #O(nlogn) time complexity
    score_to_index = {s: i for i, s in enumerate(score)}
    sorted_score = sorted(score, reverse=True)
    result = ['']*len(score)

    for i in range(len(score)):
        if i == 0:
            result[score_to_index[sorted_score[i]]]='Gold Medal'
        elif i == 1:
            result[score_to_index[sorted_score[i]]]='Silver Medal'
        elif i == 2:
            result[score_to_index[sorted_score[i]]]='Bronze Medal'
        else:
            result[score_to_index[sorted_score[i]]] = str(i + 1)
    return result

def linear_solution(score:List[int]) -> List[str]:
    pass

def solution_priority_queue(score:List[int]) -> List[str]:
    #O(nlogn) time complexity
    heap = [(-s,i) for i,s in enumerate(score)]
    heapq.heapify(heap)
    answer = ['']*len(score)

    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]

    for i in range(len(score)):
        _, index = heapq.heappop(heap)
        answer[index] = rank[i]

    return answer

def test():
    score = [10,3,8,9,4]
    score_to_index = {s: i for i, s in enumerate(score)}
    
    print(score_to_index)

def main() -> None:
    ex = [10,3,8,9,4]
    solution = solution_priority_queue(ex)
    print(solution)

if __name__ == '__main__':
    main()