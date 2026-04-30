# Day 1: Printing, Commenting, Debugging, String Manipulation and Variables

# Print() function
Print() function is used to print something


  File "e:\Learn\Day_1\main.py", line 3
    print("Hello World)
          ^
SyntaxError: unterminated string literal (detected at line 3)

Syntax Error means something is wrong with the syntax -- predefined way of writing something

Common Causes for syntax error:
1. Missing Closing Quote: The most frequent cause is simply forgetting to add the final ' or " at the end of a string.
2. Mismatched Quotes: You started the string with a single quote (') but tried to close it with a double quote (") or vice versa.
3. Ending with a Backslash (\): In Python, a backslash at the end of a string escapes the closing quote, making the interpreter think the string is still continuing.
    Incorrect: path = "C:\Users\" (The \" is treated as a literal quote inside the string, not the end of it).
    Correct: path = r"C:\Users\" (using a raw string) or path = "C:\\Users\\" (escaping the backslash).
4. Multi-line Strings: Standard single or double quotes cannot span multiple lines. If you hit "Enter" before closing the quote,    this error occurs.
    Fix: Use triple quotes (''' or """) for strings that span multiple lines.





  File "e:\Learn\Day_1\main.py", line 27
    print("Saurav")
IndentationError: unexpected indent


An IndentationError: unexpected indent occurs in Python when a line of code is shifted further to the right than it should be, or when indentation is inconsistent within a block.
Common Causes:
1. Extra Whitespace: A line has leading spaces or tabs when it is not part of a nested block (like an if statement or a function).
2. Mixing Tabs and Spaces: Python 3 does not allow mixing tabs and spaces for indentation in the same script.
3. Incorrect Block Alignment: A line within a block is indented more than the preceding line in that same block.


# Input() functions
Input() Function is used to take some values as input from users.



# Comments

# Use of hashtag # --> it will be written in code but not executed (used for single line comments)
"""
Use of three quotation--> it will be written in code but not executed too 
(Used for multi line comments)
"""


# Use of len() function

It helps to get the length of a string


# Naming Variables
1. Make sure variable names are descriptive
2. Don't have spaces between words
3. Don't start with numbers
4. Don't use special words like print or input




NameError: name 'nes' is not defined

Causes:
1. Typo in Variable or Function Name (it was sen but you type nes)
2. Variable Used Before Assignment
3. Missing Import Statement
4. Scope Issues (Local vs. Global)
5. Interactive Shell Usage