import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib.pyplot import plot, show

def jacobi(A, b, x0, tol, n_iterations=300):
    """
    Performs Jacobi iterations to solve the line system of
    equations, Ax=b, starting from an initial guess, ``x0``.

    Returns:
    x, the estimated solution
    """

    n = A.shape[0]
    x = x0.copy()
    x_prev = x0.copy()
    counter = 0
    x_diff = tol+1

    while (x_diff > tol) and (counter < n_iterations): #iteration level
        for i in range(0, n): #element wise level for x
            s = 0
            for j in range(0,n): #summation for i !=j
                if i != j:
                    s += A[i,j] * x_prev[j]

            x[i] = (b[i] - s) / A[i,i]
        #update values
        counter += 1
        x_diff = (np.sum((x-x_prev)**2))**0.5
        x_prev = x.copy() #use new x for next iteration


    print("Number of Iterations: ", counter)
    print("Norm of Difference: ", x_diff)
    return x


def cubic_spline_koefs(x, y, tol = 1e-100):
    """
    Interpolate using natural cubic splines.

    Generates a strictly diagonal dominant matrix then applies Jacobi's method.

    Returns coefficients:
    b, coefficient of x of degree 1
    c, coefficient of x of degree 2
    d, coefficient of x of degree 3
    """
    x = np.array(x)
    y = np.array(y)
    ### check if sorted
    if np.any(np.diff(x) < 0):
        idx = np.argsort(x)
        x = x[idx]
        y = y[idx]

    size = len(x)
    delta_x = np.diff(x)
    delta_y = np.diff(y)

    ### Get matrix A
    A = np.zeros(shape = (size,size))
    b = np.zeros(shape=(size,1))
    A[0,0] = 1
    A[-1,-1] = 1

    for i in range(1,size-1):
        A[i, i-1] = delta_x[i-1]
        A[i, i+1] = delta_x[i]
        A[i,i] = 2*(delta_x[i-1]+delta_x[i])
    ### Get matrix b
        b[i,0] = 3*(delta_y[i]/delta_x[i] - delta_y[i-1]/delta_x[i-1])

    ### Solves for c in Ac = b
    print('Jacobi Method Output:')
    c = jacobi(A, b, np.zeros(len(A)), tol = tol)

    ### Solves for d and b
    d = np.zeros(shape = (size-1,1))
    b = np.zeros(shape = (size-1,1))
    for i in range(0,len(d)):
        d[i] = (c[i+1] - c[i]) / (3*delta_x[i])
        b[i] = (delta_y[i]/delta_x[i]) - (delta_x[i]/3)*(2*c[i] + c[i+1])

    return b.squeeze(), c.squeeze(), d.squeeze()

def cubic_spline(X, Y):
  b, c, d  = cubic_spline_koefs(X, Y, tol = 1e-100)
  new_x, new_y = [], []
  for i, (xi, yi) in enumerate(zip(X[:-1], Y[:-1])):
    for x in np.arange(xi, X[i+1], 0.001):
      Si = yi + b[i] * (x-xi) + c[i] * (x-xi)**2 + d[i] * (x-xi)**3
      new_x.append(x)
      new_y.append(Si)
  return new_x, new_y

X = [1.5, 1.8, 2.1,	2.4, 2.7]
Y = [28, 7, 24, 87, 64]

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x, y = cubic_spline(X, Y)

plot(X, Y, color='pink', linestyle='--')
plot(x, y, color='red')
show()
