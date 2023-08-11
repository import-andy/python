"""Style Guide for Python Code"""

# Examples for PEP 8, the Style Guide for Python Code
# https://peps.python.org/pep-0008/
# https://pep8.org/
# Built-in keywords: https://docs.python.org/3.8/reference/lexical_analysis.html#keywords 

# Goals of clean coding:
    # 1. Easy to read
    # 2. Easy to understand
    # 3. Easy to change

# Two principles:
# 1. DRY - don't repeat yorself
# 2. KISS - keep it simply stupid

# Good code:
    # Readability counts
    # Code is much more read than written
    # Following a Style Guide improves readability
    # Consistency with your code is more important than with PEP 8
    # Implement version control
    # Use comments

# Code files in the core Python distribution should always use (be saved in) UTF-8.

# Self-documented code:
    # self-explanatory
    # well structured
    # uses simple programming statements
    # easy to read for others
# i.e.:
    # descriptive variable, functions, classes etc. naming

# Comments:
    # Supplement self-documented code
    # Keep them up-to-date
    # Don't use humor in comments
# Types of comments:
    # 1. Inline
    # 2. Block

# Blank lines:
    # Between methods
    # Within methods (? not python?)

# Whitespaces (spaces):
    # Before an after symbols,  e.g., a + 4 * (3 - 1), NOT a+4*(3-1).
    # Between keywords and brackets or braces

# Imports:
# Imports should be grouped in the following order:
    # 1. Standard library imports.
    # 2. Related third party imports.
    # 3. Local application/library specific imports.

import os               # Standard library imports go first
import sys              # don't use "import os, sys"
# from subprocess import Popen, PIPE - is okay to use

import xdb              # next, should be related third-party packages installed with pip

import comments         # lastly, should be local modules
import doc_strings      # don's use wildcard imports



# Naming and best practices:
# Naming conventions: https://peps.python.org/pep-0008/#naming-conventions
# AVOID the following:
    # Single letter names like o, O, I, l and L
        # except for nameing loops and index variables
    # Meaningless names
    # Names of found in __builtins__
    # Names of packages installed on the system (os, sys)

# Modules and Packages
# Naming:
    # names should be short, all lowercase, without underscores

# Classes
# Naming:
    # Should be capitalized words or capWords (camelCase)
    # Objects ARE: class Fruit (not class Eat)

# Functions and Methods
# Naming:
    # camelCase or lowercase_underscored
    # Meaningful names
    # Reveal intent
    # Use verb names (i.e. moveData)
        # Functions DO: taskKill() (not task())
    # All names should be pronouceable
# Best practices:
    # Break functions that perform more than one task

# Variables
# Naming:
    # camelCase
    # or lowercase_underscored

# 'constant' variables:
# Naming:
    # Use all uppercase with underscores.
    # usually defined on a module level
    # Examples include MAX_OVERFLOW and TOTAL.
CONSTANT = 24   

# Exceptions
# Naming:
    # Because exceptions should be classes, the class naming convention applies here (camelCase).
    # However, you should use the suffix 'Error' on your exception names
    # (if the exception actually is an error).
# Best practices:
    # Exceptions don't always need handling
    # Log everything
    # Instant response?
    # Be specific - avoid generalization

# Public or private:
    # Public interface names should not have leading underscores
    # Private interface names generally have a single leading underscore
    # Names that have 2 leading underscores will be 'mangled' (see PEP 8). To avoid clashes...
        # ...between built-in names, use a single trailing underscore ('print_' instead of 'print').


# Indentation = 4 spaces
# Tabs or Spaces?
#     - Spaces are the preferred indentation method.
#     - Tabs should be used solely to remain consistent with code that is already indented with tabs.
#     - Python disallows mixing tabs and spaces for indentation
# Lines of text should be limited to 79 characers.

# Classes' or methods' parameters:
class layout():
    pass
    
    @classmethod
    def meaningful_name_of_method(cls,                # For class method, the first parameter is called 'cls'
                                  first_parameter,    # Use indent that matches to the first delimiter
                                  second_parameter):  
        pass

    def meaningful_namr_of_method_2(
        first_long_parameter_name,       # This method can be used for long parameter names
        second_long_parameter_name,      # Use the same indent for every parameter
        third_long_parameter_name):
        pass

    def red_write(self):                # Normal methods useally use 'self' as a first parameter
        with open('some really long address///sdmdgdkgmldkfmvlvdmls') as file_source, \
        open('some really long address///sdmdgdkgmldkfmvlvdmls') as file_dest:         # Backslashes for continuous strings 
            some_addressvmf


# Hanging indent:

# yes:
    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                            var_three, var_four)

    # More indentation included to distinguish this from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

    # Hanging indents should add a level.
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)

# No:
    # Arguments on first line forbidden when not using vertical alignment.
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    # Further indentation required as indentation is not distinguishable.
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)


