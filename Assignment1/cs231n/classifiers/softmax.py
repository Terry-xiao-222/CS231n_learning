import numpy as np
from random import shuffle


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    for i in range(num_train):
        scores = X[i].dot(W)

        # compute the probabilities in numerically stable way
        scores -= np.max(scores)  # 有广播，标量可以自动扩展，复制成和左边(C,)一模一样大小的数组
        ## a code trick:防止计算 np.exp(scores) 时发生数值溢出，同时完全不改变 Softmax 的最终概率，所谓的numerically stable
        exp_scores = np.exp(scores)
        probabilities = exp_scores / np.sum(exp_scores)

        loss += -scores[y[i]] + np.log(np.sum(exp_scores))

        for j in range(num_classes):
            coefficient = probabilities[j]

            if j == y[i]:
                coefficient -= 1.0

            dW[:, j] += coefficient * X[i]

    loss /= num_train
    dW /= num_train

    loss += reg * np.sum(W * W)
    dW += 2.0 * reg * W

    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather that first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    num_classes = W.shape[1]
    num_train = X.shape[0]

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the softmax loss, storing the           #
    # result in loss.                                                           #
    #############################################################################

    # 1. Compute scores for all examples.
    # (N, D) @ (D, C) -> (N, C)
    scores = np.dot(X, W)

    # 2. Improve numerical stability.
    # Subtract the maximum score in each row.
    scores -= np.max(scores, axis=1, keepdims=True)

    # 3. Compute Softmax probabilities.
    # Both exp_scores and probabilities have shape (N, C).
    exp_scores = np.exp(scores)
    sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)
    probabilities = exp_scores / sum_exp_scores

    # 4. Compute the average cross-entropy loss.
    correct_scores = scores[np.arange(num_train), y]

    loss = np.mean(-correct_scores + np.log(sum_exp_scores[:, 0])) # sum_exp_scores[:, 0]:(N, 1) ——> (N,) 

    # Add L2 regularization loss.
    loss += reg * np.sum(W ** 2)

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the softmax            #
    # loss, storing the result in dW.                                           #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################


    # 5. Compute the gradient with respect to scores.
    # For each example:
    # dscores = probabilities - one_hot_labels
    dscores = probabilities.copy()
    dscores[np.arange(num_train), y] -= 1.0
    dscores /= num_train

    # 6. Compute the gradient with respect to W.
    # (D, N) @ (N, C) -> (D, C)
    dW = X.T @ dscores

    # Add the gradient of L2 regularization.
    dW += 2.0 * reg * W

    return loss, dW
