import sys
from File import File
from LexicalAnalyser import LexicalAnalyser
from SemanticAnalyser import SemanticAnalyser
from SyntaticAnalyser import SyntaticAnalyser
from ThreeAddressCodeParser import ThreeAddressCodeParser

if __name__ == '__main__':
    file_path = sys.argv[1]

    file = File(path=file_path)
    lexical = LexicalAnalyser()

    file.read()
    for line in file.buffer:
        lexical.analyse(line)

    syntatic = SyntaticAnalyser()
    syntatic.analyse(lexical.data)

    if not syntatic.has_error:
        semantic = SemanticAnalyser()
        semantic.analyse(lexical.data)

    IC = ThreeAddressCodeParser(lexical.data)
    IC.parse()