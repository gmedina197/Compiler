from File import File
from LexicalAnalyser import LexicalAnalyser

if __name__ == '__main__':
    file = File()
    lexical = LexicalAnalyser()

    file.read()
    for line in file.buffer:
        lexical.analyse(line)
    
    lexical.print_tokens()