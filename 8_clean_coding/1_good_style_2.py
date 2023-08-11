"""Style Guide for Python Code 2"""

# Types of languages:
    # Strongly typed
        # promote clean coding i.e. Java
    # Weakly typed
        # i.e. Python

# Identifiers - variables, functions & etc...
# Identifiers should be:
    # Readable 
        # no abbreviations or cryptic names
    # Meaningful
        # should indicate the purpose of content
        # class names should indicate function/purpose
    # Uniue
    # Short
        # except for nameing loops and index variables
    # Consistent
        # syntactically & semantically

# Styles:
    # 1. camelCasing
    # 2. delimiter_separated
    # 3. strLastName - hungarian notation: data type + content using camel casing
    # 4. PascalCase - first letter is also capped unlike camel casing


# Cohesion:
# Refers to how closely elements are related
    # 1. High cohesion
    # 2. Low cohesion

# Types of return values:
    # 1. Flags - 0 or 1
    # 2. Single values
    # 3. Sequence types (list, etc...)

# One function - one action (singular focus).
# It makes it easier to work with & troubleshoot.
    # i.e. data access & data validation - 2 different functions.

# Capabilities provided by the classes:
    # 1. Abstraction - manages levels of complexity
        # from complex (lower) to simpler (higher)
    # 2. Encapsulation - data hiding
    # 3. Inheritance - best practice is three levels or fewer
        # typically, shoulb be used, when there is a "is a", (apple -> fruit)
        # relationship, not "has a" (car -> wheels)
    # 4. Polymorphism
    # 5. Modularity
    # 6. Domain modeling

# Constructors - special types of methods in a class,
# used to create and initialize an instance of an object


# A typical project structure:
    # - build (or dist)
    # - docs (or doc)
    # - src (or lib or app)
    # - test (or spec)
    # - tools
    # - LICENSE
    # - README.md