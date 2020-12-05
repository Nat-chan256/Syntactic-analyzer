from SyntacticAnalyzer import SynatcticAnalyzer
from GraphematicAnalyzer import GraphematicAnalyzer
from MorphologicalAnalyzer import MorphologicalAnalyzer
from nltk.draw.tree import draw_trees

FILE_NAME = "Test files\\" + "simpleSents.txt"

try:
    file = open(FILE_NAME, "r", encoding="UTF-8")
    text = file.read()
    file.close()

    graphAn = GraphematicAnalyzer()
    proccessedText = graphAn.sentences(text)
    for sentence in proccessedText:
        parserResult = SynatcticAnalyzer.analyzeSentence(sentence)
        draw_trees(*(tree for tree in parserResult))

    #morph = MorphologicalAnalyzer()
    #for a in morph.analyzeWord("прибрано"):
    #    print(a['часть речи'])
    
except FileNotFoundError:
    print("The file does not exist")