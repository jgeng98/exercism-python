def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores = []
    for i in range(3):
        top_scores.append(max(scores))
        scores.remove(top_scores[i])
        if len(scores) == 0:
            break
    return top_scores
