from File import File
from LexicalAnalyser import LexicalAnalyser

if __name__ == '__main__':
    file = File()
    a = LexicalAnalyser()

    file.read()
    for line in file.buffer:
        a.analyse(line)
    
    a.print_data()