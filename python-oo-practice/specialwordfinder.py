from wordfinder import WordFinder

class Special_word_finder(WordFinder):
    def __init__(self, file):
        super().__init__(file)
    def readfile(self):
        """Reads the file into list, but omits blank lines and comments"""
        openfile = open(self.file,"r")
        for line in openfile:
            stripped = line.strip()
            if len(stripped) > 0 and not stripped[0] == "#":
                self.list.append(line.strip())
        openfile.close()