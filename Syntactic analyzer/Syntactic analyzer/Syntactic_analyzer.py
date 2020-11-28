from SyntacticAnalyzer import SynatcticAnalyzer

FILE_NAME = "Test files\\" + "Samples.txt"

try:
    parserResult = SynatcticAnalyzer.analyzeSentence("Мама мыла грязную раму")

    for tree in parserResult:
        print(tree)

except FileNotFoundError:
    print("The file does not exist")