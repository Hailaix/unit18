"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """Class that takes a file with words seperated by line
    and allows for random words from that file to be returned
    """
    def __init__(self, file):
        self.file = file
        self.list = []
        self.readfile()
        print(f"{len(self.list)} words read")

    def readfile(self):
        """reads the file and places each line into list"""
        openfile = open(self.file,"r")
        for line in openfile:
            self.list.append(line.strip())
        openfile.close()
    def random(self):
        """returns a random word from the list"""
        return self.list[randint(0,len(self.list)-1)]