import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    X = np.array(x)
    max_logits = np.max(X,axis=-1,keepdims=True)
    exp_logits = np.exp(X-max_logits)

    sum_exp = np.sum(exp_logits,axis=-1,keepdims=True)
    probabilities = exp_logits/sum_exp

    return probabilities
    
    