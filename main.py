from File import File
from LexicalAnalyser import LexicalAnalyser

if __name__ == '__main__':
    file = File()
    a = LexicalAnalyser()

    file.read()

    a.analyse(file.buffer[0])