
## Probability of the given labels for all datapoints

We will now train our logistic regression model on a training dataset. This dataset contains a number of datapoints $\x_1,\dots,\x_N$belonging to two classes and, for each datapoint $\x_n$, the corresponding class label $\c_n$. The training is done by *maximum likelihood*, that is, we maximise the probability of the data given the model. 

## Model

Before we start coding, let's have a closer look at the model. Our labels are $0$ or $1$, representing the two classes. If a datapoint $\x_n$ belongs to class $\c_n=1$, the probability $p(\c_n=1|\x_n) = \sigma(\w^\top\x_n)$; otherwise, the probability $p(\c_n=0|\x_n) = 1-\sigma(\w^\top\x)$ (where $\x$ denotes a datapoint which is extended with a constant $1$ as the first dimension, so that the inner product includes the bias $w_0$). We now want the probability of the labels given the data, for the complete training set: $p(\c_1,\dots,\c_N|\x_1,\dots,\x_N)$. Remember that the probability of the union of two independent events is $p(a,b)=p(a)\,p(b)$. Using the fact that the labels are $0$ and $1$ (and that $x^0=1$ and $x^1=x$, we can then write this as 
$$p(\c_1\dots\c_n|\x_1\dots\x_n,\w) = \prod_{n=1}^N \sigma(\w^\top\x_n)^{\c_n}\,(1-\sigma(\w^\top\x_n))^{1-\c_n}$$

**Question 1:** For the provided dataset, compute this probability when the model weights are $\w = [ 0,-1,-1]$. Is the computed answer what you expected? Is it exactly correct?
Think about how you could find the maximum of this function. What does the gradient of this probability look like (that is, if I changed the value of $\w$ a little bit, how would the probability change)?
