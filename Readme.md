Expression Evaluator:

This Python code evaluates mathematical expressions containing numbers, operators (`+`, `-`, `*`, `/`), and parentheses using two stacks: one for numbers and one for operators.

 How It Works:

- Stacks: 
  - s1: Stores numbers.
  - s2: Stores operators and parentheses.
  
- Parsing: The code traverses the input string, pushing numbers onto `s1` and applying operators based on their precedence.

- Operator Precedence: Managed by the val() method to ensure correct order of operations.

- Parentheses: Used to control the order, allowing sub-expressions to be evaluated first.

- Output: The final result is computed by popping values and operators from the stacks and is printed after processing the entire expression.


Example: 

For the expression `2*(2+200)`, the output will be `404`.

Usage:

Simply call the `evaluate_expression()` method to evaluate any valid mathematical expression.
