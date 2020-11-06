from GraphematicAnalyzer import GraphematicAnalyzer

FILE_NAME = "Test files\\" + "Samples.txt"


try:
    file = open(FILE_NAME, encoding="utf8")
    text = file.read()
   
    graphAnalyzer = GraphematicAnalyzer()
    tokens = graphAnalyzer.createTableWithDescriptors(text)
    
    for token in tokens:
        print(token)

    file.close()
except FileNotFoundError:
    print("The file does not exist")