## Q1

### Intuition
When calculating the maximum value of $U$, we aim to maximize the product of some data elements while minimizing the product of their reciprocals.

Let’s assume the integer data set is $(x_1, x_2, \ldots, x_n)$, where (n) represents the number of data points. Our goal is to find a subset (S) that maximizes the following formula:

$U = \left(\prod_{i \in S} x_i\right) \left(\prod_{i \notin S} \frac{1}{x_i}\right)$

If (U) is positive:
We want to maximize the product of the positive data elements, $\left(\prod_{i \in S} x_i\right)$
Simultaneously, we want to minimize the product of the reciprocals of the negative data elements, $\left(\prod_{i \notin S} \frac{1}{x_i}\right)$.

If (U) is negative:
We aim to minimize the product of the positive data elements, $\left(\prod_{i \in S} x_i\right)$.
At the same time, we seek to maximize the product of the reciprocals of the negative data elements, $\left(\prod_{i \notin S} \frac{1}{x_i}\right)$.

### Algorithm
1. Determine the Sign of (U)
2. Identify Subset (S) according to the Sign of (U)
   - If the sign of (U) is positive,then:
   >Select Larger Absolute Values for (S):
We aim to maximize the product of the positive data elements, $\left(\prod_{i \in S} x_i\right)$.
Therefore, we should include data points with larger absolute values in subset (S).
Use Smaller Absolute Values for the Reciprocal Product:
To minimize $\left(\prod_{i \notin S} \frac{1}{x_i}\right)$, we should use smaller absolute values.
Hence, we include data points with smaller absolute values in the reciprocal product.
   - If the sign of (U) is negative,the logic reverses.
3. Calculate the U value according to the two formulas given in the question.



## Q2
### Intuition
We have two lists: team A representing the goals scored by Team A in their matches, and team B representing the goals scored by Team B in their matches.
For each match of Team B, we need to find how many matches of Team A had scores less than or equal to the goals scored by Team B in that match.

### Algorithm
For this question, $sum$ method in Python can be useful.

## Q3

**Initialization (`__init__` method):**

- The constructor initializes an empty stack (`self.data`) and sets the length of the stack to 0 (`self.length`).
- The stack is represented as a list.

**Printing the Top Element (`print_top` method):**

- If the stack is empty (length is 0), it prints “EMPTY.”
- Otherwise, it prints the last element in the stack (`self.data[-1]`).

**Pushing an Element onto the Stack (`push` method):**
- Accepts an integer value `v`.
Checks if `v` is an integer; if not, raises a TypeError.
- Increments the stack length by 1.
- Appends v to the stack.
- Calls `print_top()` to display the new top element.

**Popping an Element from the Stack (`pop` method):**
- Removes the last element from the stack (`self.data.pop()`).
- Decrements the stack length by 1.
- Calls `print_top()` to display the new top element.
- Returns the popped value.

**Incrementing Elements in a Range (`inc` method):**
Accepts two integers: `i`(index) and `v` (value).
Modifies the first `i` elements of the stack by adding `v` to each element.
Calls `print_top()` to display the new top element.

**Overall, this class implements a basic stack with push, pop, and increment operations.** The `inc` method allows modifying a specific range of elements in the stack. The `print_top` method ensures that the top element is displayed correctly. The stack is maintained using a list (`self.data`).