import sys
from File import File
from LexicalAnalyser import LexicalAnalyser
from SemanticAnalyser import SemanticAnalyser
from SyntaticAnalyser import SyntaticAnalyser

if __name__ == '__main__':
    file_path = sys.argv[1]

    file = File(path=file_path)
    lexical = LexicalAnalyser()

    file.read()
    for line in file.buffer:
        lexical.analyse(line)

    syntatic = SyntaticAnalyser()
    syntatic.analyse(lexical.data)

    if syntatic.has_error:
        print('Error')
    else:
        semantic = SemanticAnalyser()
        semantic.analyse(lexical.data)
