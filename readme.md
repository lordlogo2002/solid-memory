# solid-memory

This is a simple calculator program that performs single operations on two numbers. It allows the user
to input two integer or float values, along with an operator to perform the calculation. The calculator
supports various operations, and you can even add your own custom operators. The program also offers the
option to activate or deactivate colored output.

 - This idea is inspired by: [@MakiWolf)] ([https://www.github.com/username](https://github.com/MakiWolf))
 - project: https://github.com/MakiWolf/easysimplifiedcalculator1

## Usage

1. Run the main.py script.
2. Follow the instructions displayed on the screen.
3. Enter the first number.
4. Enter the desired operator from the available options. For example, to perform addition, enter "+". You
   can use the following operators: addition (+), subtraction (-), division (/), multiplication (*),
   modulus (%), or random number generation (#).
5. Enter the second number.
6. The program will calculate the result and display it.
7. You can choose to start another calculation by entering the restart keyword ("1"), or stop the program
   by entering any other input.

## Adding Custom Operators

### To add your own custom operators, follow these steps:

1. Open the operations.py file.
2. Define your operator as a lambda function that takes two arguments and performs the desired calculation. For example, to define a custom operator "**" for exponentiation, you can
   use the following code:

     ```python
     exp = lambda a, b: a ** b
     ```

3. Add your operator to the OPERATIONS dictionary using the desired math symbol as the key and the lambda function as the value. For example, to add the "**" operator, modify the
   OPERATIONS dictionary as follows:

    ```python
    OPERATIONS = {
        "+": add,
        "-": sub,
        "/": div,
        "*": mul,
        "%": mud,
        "#": rnd,
        "**": exp
    }
    ```

4. Save the operations.py file.

#### You can now use your custom operator in the calculator by entering the corresponding math symbol.

## Activating/Deactivating Colored Output

By default, the calculator program displays colored output using the `colored` module, which internally uses `colorama`. However, you can choose to activate or deactivate colored output by modifying the program.

To set the flag for color activation or deactivation, follow these steps:

1. Open the `colored.py` file.
2. Locate the `MetaColor` class definition.
3. Inside the `MetaColor` class, find the `use_color` flag and set it accordingly:
   - Set `use_color = True` to activate colored output.
   - Set `use_color = False` to deactivate colored output.

   Here's an example of how the `MetaColor` class should look with the `use_color` flag set:

    ```python
    class MetaColor(type):
        use_color = True
    ```

4. Save the colored.py file.
