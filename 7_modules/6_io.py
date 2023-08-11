"""input-output built-in module"""

import io

# Technically, you don't need to import io module to do inpus & outpts. Like here:
with open('log.txt', 'w') as write_file:
    to_log = input('What do you want to write to the log? ')
    write_file.write(to_log)