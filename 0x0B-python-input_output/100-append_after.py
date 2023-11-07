#!/usr/bin/python3
"""13. Search and update

function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string
    """
    readlines = []
    newtext = []
    with open(filename, 'r') as f:
        readlines = f.readlines()

    for line in readlines:
        newtext.append(line)
        if search_string in line:
            newtext.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(newtext)
