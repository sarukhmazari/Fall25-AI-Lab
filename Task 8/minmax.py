import math

def minimax(current, nodeIndex, maxTurn, scores, target):
    if current == target:
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(current + 1, nodeIndex * 2, False, scores, target),
            minimax(current + 1, nodeIndex * 2 + 1, False, scores, target)
        )
    else:
        return min(
            minimax(current + 1, nodeIndex * 2, True, scores, target),
            minimax(current + 1, nodeIndex * 2 + 1, True, scores, target)
        )
scores = [3, 5, 2, 9, 3, 5, 2, 9]
target = int(math.log(len(scores), 2))

print("the best value is:", minimax(0, 0, True, scores, target))
