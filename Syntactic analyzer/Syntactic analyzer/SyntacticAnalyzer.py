from enum import Enum
import nltk

from GraphematicAnalyzer import GraphematicAnalyzer
from MorphologicalAnalyzer import MorphologicalAnalyzer

class SynatcticAnalyzer:

    #Takes a text of string type, returns parse tree (or trees) 
    def analyzeSentence(sentence):
        sent = GraphematicAnalyzer.words(sentence)
        #Create grammar file with words from the sentence
        try:
            GRAMMAR_FILE_NAME = "grammar.txt"
            NEW_GRAMMAR_FILE_NAME = "new_grammar.txt"

            gramFile = open(GRAMMAR_FILE_NAME, "r", encoding="UTF-8")
            newGramFile = open(NEW_GRAMMAR_FILE_NAME, "w", encoding="UTF-8")

            #Copy grammar from existing file to new file
            line = gramFile.read()
            while line:
                newGramFile.write(line)
                line = gramFile.read()
                
            #Collect words to be written to the new grammar file
            posDict = {}
            for word in sent:
                for analysisResult in MorphologicalAnalyzer.analyzeWord(word):
                    if analysisResult['часть речи'] in posDict.keys():
                        posDict[analysisResult['часть речи']].append(word)
                    else:
                        posDict[analysisResult['часть речи']] = [word]

            #Write collected words to the new grammar file
            for pos in posDict.keys():
                curStr = pos + " -> ";
                for i in range(len(posDict[pos]) - 1):
                    curStr += "'" + posDict[pos][i] + "'" + " | "
                curStr += "'" + posDict[pos][len(posDict[pos])-1] + "'"
                newGramFile.write("\n" + curStr)

            gramFile.close()
            newGramFile.close()

            #Read new grammar from file
            f = open(NEW_GRAMMAR_FILE_NAME, "r", encoding="UTF-8")
            g = f.read()
            f.close()

            #Build trees for each sentence
            grammar = nltk.CFG.fromstring(g) 
            #rd_parser = nltk.RecursiveDescentParser(grammar)
            rd_parser = nltk.ChartParser(grammar)
            return rd_parser.parse(sent)

        except Exception as ex:
            print(f"Ошибка: {ex}")
            return []