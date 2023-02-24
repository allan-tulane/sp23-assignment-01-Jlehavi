

# CMPS 2200 Assignment 1

**Name:**_Jack Lehavi___


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?
.    Based on the definiotn, 2^(n+1) <= O(2^n)It is in O(2^n) because the equation 0 <= 2^{n+1} <= c*2^n must be true. For a c value of 2, the equation is true : 0<= 2^{n+1} <= 2^{n+1}. Therefore, the original statement is true.
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  This is not true. Using the same formula 0 <= 2^{2^n} <= c*2^n we can prove this. If we take the log of both sides, we can simplify the equation to : 2^n * log(2) <= n * log(c*2). Knowing that the higher power in equations asymptotically dominates, 2^n > n. Thus, the first equation is not in O(2^n).
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?
    Based on the definition, n^1.01 <= c * log^2 n for any number c and n > n0. We know n^1.01 is a higher ordered function than log^2 n which means n^1.01 grows faster than log^2 n. This function is only true for 0<n<~0.5. Thus the function is not true for any number c. 
.  
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Based on the definiton, n^1.01 >= c * log^2 n for any number c and any n > n0. We know that n^1.01 is a higher ordered function than log^2(n). n^1.01 is greater than log^2(n) for all n > ~.5. Thus, n^1.01 is in Omega(log^2(n)).
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  Based on the definition, sqrt(n) <= c * (logn)^3 for any number c. We know that sqrt(n) is a higher power than log(n) so for any c the equation would never be true. Thus, sqrt(n) is not in O(log()^3).
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Based on the definition, sqrt(n) >= c * (log(n))^3 for any number c. We know that sqrt(n) is a higher ordered function than log(n) so sqrt(n) will always be larger than c * log(n) for any number c. Thus, sqrt(n) is in Omega (log(n)^3).


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
    The first number you input into the function is the index of the number you are trying to find within the fibonacci sequence. The function works backwards until the base case is reached and recursively sums all the values of the fibonacci sequence until the index provided is reached and finally returns the sum.
.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
      Work: O(n)
      Span: O(n)
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  Work: O(n)
.  Span: O(log(n))
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
    Work: O(nlog(n))
    Span: O(log(n))
.  
.  
.  
.  
.  
.  
.  
.  

