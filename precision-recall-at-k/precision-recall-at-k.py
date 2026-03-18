def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    rel = set(relevant)
    count = 0
    for i in range(k):
        if top_k[i] in rel: 
            count = count + 1
    precision_at_k = count/k
    recall_at_k = count/len(relevant)
    return [precision_at_k, recall_at_k]