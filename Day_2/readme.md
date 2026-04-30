# Day 2: Data Types, f-strings, type conversion

TypeError: object of type 'int' has no len()
Causes:
1. Direct call on a number: You might have written something like len(100).
2. Variable confusion: A variable you thought was a list or string was actually assigned an integer.
3. Accidental reassignment: You might have started with a list but later replaced it with a single number (e.g., in a loop or     after a function return).


ValueError: invalid literal for int() with base 10: 'abc'
Causes:
1. Alphabetic characters: Trying to convert a string like 'abc' or '123a'.
2. Empty strings: Passing "" to int().
3. Floating-point numbers: Passing a string with a decimal point, like '1.5'. Note that int() cannot directly convert decimal strings; you must use float() first.
4. Special symbols: Strings containing spaces, commas, or currency symbols (e.g., '$100').