# activity for errors

# Create the FileManipulator class and implement the constructor.
# The constructor should accept the name of a file to read in and
# should continually prompt for input if the name given causes an
# error. Make sure that you give an informative message if an error
# is raised.

class FileManipulator:
    def __init__(self, fileName):
        self.contents = None
        while self.contents == None:
            try:
                myfile = open(fileName, 'r') # Open a file for reading.
                self.contents = myfile.readlines() # Read in the content by line.
            except (FileNotFoundError, TypeError, OSError) as e:
                print(type(e), e)
                fileName = input("Please enter the name of the file you would like to read: ")
            else:
                myfile.close() # Explicitly close the file

# Implement the reverse() function. This function should accept the
# name of a file to write to and should write each line of the
# original file to this new file. However, in the new file, although
# the line order will be the same, the string that makes each line
# will be reversed. So "cheese" will become "eseehc". Be careful
# not to add an extra newline character at the beginning of the file.
# Make sure that errors are handled elegantly, and appropriate error
# messages are given.

def reverse(self, fileName):
    while True:
        try:
            myfile = open(fileName, 'w')
            revContent = [x.strip()[::-1] for x in self.contents]
            for i in range(len(revContent)):
                if i == (len(revContent)-1):
                    myfile.write(revContent[i])
                else:
                    myfile.write(revContent[i] + '\n')
        except (FileNotFoundError, TypeError, OSError) as e:
            print(type(e),e)
            fileName = input("Please enter a valid file name: ")
        else:
            myfile.close()
            break


# test code:
f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
