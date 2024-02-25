## Setup
I am using  [`Poetry`](https://github.com/python-poetry/poetry)to manage my development environment. If you are also using `Poetry`, you can configure and install the environment by using `Poetry install`.
My development environment is:
- `MacOS Monterey`
- `Python 3.12`
- The only additional dependency I install is `Pytest`

1. **Install Dependencies:**
Run the following command to install your package’s dependencies: ```poetry install```

2. **Run Tests:**
Execute your tests using the following command: ```poetry run pytest```

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

### Tests
**test_odd_with_positive_numbers:**
- Input: `[1, 2, 3, 4, 5]`
- Result: `[3, 4, 1, 5, 2]`
- U value: `30`

**test_odd_with_negative_numbers:**
- Input: `[-1, -2, -3, -4, -5]`
- Result: `[-3, -2, -5, -1, -4]`
- U value: `-0.3`
  
**test_even_with_positive_numbers:**
- Input: `[1, 2, 3, 4, 5, 6]`
- Result: `[2, 3, 1, 4, 5, 6]`
- U value: `720`
  
**test_even_with_negative_numbers:**
- Input: `[-1, -2, -3, -4, -5, -6]`
- Result: `[-6, -5, -1, -4, -3, -2]`
- U value: `720`
  
**test_even_mixed_with_positive_and_negative_numbers:**
- Input: `[1, 2, 3, -4, -5, -6]`
- Result: `[-5, -4, -6, 1, 2, 3]`
- U value: `-20.0`
  
**test_odd_mixed_with_positive_and_negative_numbers:**
- Input: `[1, 2, 3, -4, -5]`
- Result: `[-5, -4, 1, 3, 2]`
- U value: `30`
  
**test_numbers_with_zero:**
- Input: `[-5, 0, 0, 0, 0]`
- Result: `[-5, 0, 0, 0, 0]`
- U value: `0`
  
**test_empty_input:**
- Input: `[]`
- Result: `[]`
- U value: `None`

**test_numbers_with_non_integer_elements:**
- Input: `[1, 2, 3, "c", "a"]`
- Result: `[1, 2, 3, "c", "a"]`
- U value: `None`

## Q2
### Intuition
We have two lists: team A representing the goals scored by Team A in their matches, and team B representing the goals scored by Team B in their matches.
For each match of Team B, we need to find how many matches of Team A had scores less than or equal to the goals scored by Team B in that match.

### Algorithm
For this question, $sum$ method in Python can be useful.

### Tests
1. **test_find_matches_normal_case_1:**
- Input: `team_a = [1, 2, 3]`, `team_b = [2, 4]`
- Expected output: `[2, 3]`

2. **test_find_matches_normal_case_2:**
- Input: team_a = `[1, 2, 3]`, team_b = `[2, 4, 5, 6]`
- Expected output: `[2, 3, 3, 3]`

3. **test_find_matches_with_one_empty_list_1:**
- Input: `team_a = []`, `team_b = [2, 4, 5, 6]`
- Expected output: `[0, 0, 0, 0]`

4. **test_find_matches_with_one_empty_list_2:**
- Input: `team_a = [1, 2, 3]`, `team_b = []`
- Expected output: `[]`

5. **test_find_matches_with_two_empty_lists:**
- Input: team_a = `[]`, team_b = `[]`
- Expected output: `[]`

6. **test_find_matches_with_non_integer_elements:**
- Input: `team_a = ["243"]`, `team_b = [1, 2, 3, 4]`
- Expected output: `[]`

7. **test_find_matches_with_none:**
- Input: `team_a = None`, `team_b = None`
- Expected output: `[]`

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

### Tests
1. **test_push:**
- Purpose: Tests the `push` method.
- Input: Pushes integers 1, 2, and 3 onto the stack.
- Expected output: The stack’s data should be `[1, 2, 3]`.
  
2. **test_pop:**
- Purpose: Tests the `pop` method.
- Input: Pushes integers 1, 2, and 3 onto the stack, then pops an element.
- Expected output: The stack’s data should be `[1, 2]`.
  
3. **test_inc:**
- Purpose: Tests the `inc` method.
- Input: Pushes integers 1, 2, and 3 onto the stack, then add 2 to each of the bottom 2 elements of the stack
- Expected output: The stack’s data should be `[3, 4, 3]`.
  
4. **test_normal_case:**
- Purpose: Tests a combination of `push`, `pop`, and `inc` operations.
- Input: Pushes integers 1, 2, and 3 onto the stack, then add 2 to each of the bottom 2 elements of the stack, and then pops an element.
- Expected output: The stack’s data should be `[3, 4]`.
  
5. **test_pop_from_empty_stack:**
- Purpose: Ensures that popping from an empty stack raises an `IndexError`.
- Expected behavior: An `IndexError` should be raised.
  
6. **test_inc_on_empty_stack:**
- Purpose: Tests the `inc` method on an empty stack.
- Input: Increments an empty stack by 1.
- Expected output: The stack remains empty.
  
7. **test_push_with_non_integer_element:**
- Purpose: Ensures that adding non-integer elements to the stack - raises a `TypeError`.
- Expected behavior: A `TypeError` should be raised.