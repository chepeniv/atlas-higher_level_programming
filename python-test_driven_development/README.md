# TEST DRIVEN DEV: 
## Guidance

- always write the documentation and tests first, before actually coding anything
- intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- work together on test cases, so that you don’t miss any edge case
- don’t ever trust the user, always think about all possible edge cases

## Objectives
- what’s an interactive test ?
- why tests are important ?
- how to write docstrings to create tests ?
- how to write documentation for each module and function ?
- what are the basic option flags to create tests ?
- how to find edge cases ?


## Requirements

- first line of all files should be `#!/usr/bin/python3`
- code should use pycodestyle (version 2.7.+)
- a documentation is not a single word, it’s a complete sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- all modules should have documentation : 
		`python3 -c 'print(__import__("my_module").__doc__)'`
- all classes should have documentation : 
		`python3 -c 'print(__import__("my_module").myclass.__doc__)'`
- all functions (inside and outside a class) should have a documentation :
		`python3 -c 'print(__import__("my_module").my_function.__doc__)'`\
		`python3 -c 'print(__import__("my_module").myclass.my_function.__doc__)'`

## Testing

- test files should be inside a folder tests
- test files should be .txt files 
- tests should be executable via `python3 -m doctest ./tests/*`
