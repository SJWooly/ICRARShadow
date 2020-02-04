# A function that took too long to write but proved me solid point on using documentation
# Finds which string element of a list contains the search string, then replaces it
# 21 Jan 2020


readfile = 'local_cybershake_100'
search = 'xmlns'
replacement = '<adag version="2.1" count="1" index="0" name="test" jobCount="25" fileCount="0" childCount="20">\n'
                # needs backslh n for new line


def editUselessString(filename, searchString, replacementString):
    edittedStrings = []
    with open(filename, 'r') as infile:
        for line in infile:
           if line.find(searchString) >=0:
               edittedStrings.append(replacementString)
           else:
               edittedStrings.append(line)
    return edittedStrings

newListOfLines = editUselessString(readfile, search, replacement)


def replaceOldString(filename):
    with open(filename, 'w+') as outfile:
        for line in newListOfLines:
            outfile.write(line)
replaceOldString(readfile + "_editNS")