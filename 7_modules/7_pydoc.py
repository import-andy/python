# PyDoc module

# PyDoc module automatically generates documentation from Python modules. 
# The documentation can be presented as pages of text on the console, served to a web browser, or saved to HTML files.
    # The difference between PyDoc & help():
        # 1. With PyDoc you don't have to import modules for their documentation
        # 2. PyDoc works from the console (not through the python intercative mode)
        # 3. PyDoc can search all modules for a certain keyword
# PyDoc can generate web-pages from your documentation
# Documentation often takes more space, then the code itself

# python -m pydoc              # '-m' running PyDoc module. Can see it's uses here:
    # python -m pydoc <name>
    # python -m pydoc -k
    # python -m pydoc -n
    # python -m pydoc -p
    # python -m pydoc -b
    # python -m pydoc -w

# pythom -m pydoc math         # Documrntation for 'math' module
# python -m pydoc tuple
# python -m pydoc pow

# python -m pydoc              # Searching all modules for a certain keyword
# python -m pydoc -k ftp
# python -m pydoc -k sql

# python -m pydoc -p 314       # SUPER USEFUL. Starting an HTTP server with the given hostname. Idk why exactly '314'
# python -m pydoc -b           # Same as above, but starts at a random unused port.

# >mkdir pydoc_demo            # create a new folder
# >cd pydoc_demo               # go to that folder
# python -m pydoc -w json      # Run '-w' on some class/type/module - creating an HTML file for documentation
                               # This is useful, when you want to save your PyDoc documentation on a separate server