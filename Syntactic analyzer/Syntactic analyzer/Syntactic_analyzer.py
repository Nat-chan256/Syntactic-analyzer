from SyntacticAnalyzer import SynatcticAnalyzer
from nltk.draw.tree import draw_trees

FILE_NAME = "Test files\\" + "Samples.txt"

try:
    parserResult = SynatcticAnalyzer.analyzeSentence("Мама мыла грязную раму")

    #for tree in parserResult:
    #    print(tree)

    draw_trees(*(tree for tree in parserResult))

except FileNotFoundError:
    print("The file does not exist")