def knn_predict(p, points, outcome, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcome[ind])
