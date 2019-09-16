"""Assignment 1

NOTE: I strongly recommend you read the whole assignment file BEFORE
starting on the project.

Get yourself started with a development environment and write some
code and look at the Python documentation.

For 90%:
* Fill in the fac function with an implementation of the factorial
  function.
* And the fib function with an implementation of Fibonacci.
* And the linear_fib function as it's documentation specifies.

For 100%:
* Implement fac without writing any recursion or iteration, and
  using one standard library function and the product function below.
  Look up the range function.

None of your code should print any output. If you want to have some
debugging prints you do not have to remove, look up and use the
logging package in the standard library.

You will be penalized for removing or misplacing docstrings or
formatting your code poorly.

See:
https://docs.python.org/3/library/functions.html

Feel free to use any code you find in the Python documentation.
However you should cite the source of the code in a comment.


NOTE: `raise NotImplementedError()` is a standard way to mark methods
that still need to be implemented. Remove it along with the TODOs
when you have implemented the methods.

"""

import functools

def product(l):
    """Compute the product of all elements of the iterable l."""
    def times(x, y):
        return x * y
    return functools.reduce(times, l)

def fib(n):
    """Compute the n-th Fibonacci number.

    Recursive fib implementations are simpler and simpler code will
    get you more points. This function does not need to be fast.

    Note: fib(0) is 0, and fib(1) is 1.

    """
    # raise NotImplementedError()
    if n==0:
        fibonacci=0
    elif n==1:
        fibonacci=1
    else:
        fibonacci = fib(n-1) +fib(n-2)   
    return fibonacci          

def fac(n):
    """Compute n! (n factorial).

    Note: fac(0) is 1.
    """
    if n==1:
        factorial = 1
    else:
        factorial = n*fac(n-1)       

    # raise NotImplementedError()
    return factorial



def linear_fib(n):
    """Compute fib(n) in O(n) time using memoization and recursion.

    Use a global variable and one of the data structures you have
    learned about to implement a linear time recursive Fibonacci. Use
    memoization; it is possible to implement Fibonacci in linear time
    without memoization (using a loop), but that is not the
    assignment.

    Remember to look at the Python library documentation for any
    data structure needs you have.
    """
    # raise NotImplementedError()
    fn = f1 = f2 = 1
    for x in range(2, n):
        fn = f1 + f2
        f2, f1 = f1, fn
    return fn




