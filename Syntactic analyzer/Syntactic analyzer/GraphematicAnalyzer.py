from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
import itertools
import string

class GraphematicAnalyzer:

    #Takes the text of string type, returns the list of paragraphs
    def divideIntoParagraphs(self, text):
        paragraphs = text.split("\n")
        return paragraphs

    #Takes the text of string type, returns the list of sentences
    def divideIntoSentences(self, text):
        sentencesList = sent_tokenize(text)
        return sentencesList

    #Takes the text of string type, returns the list of words
    def divideIntoWords(self, text, includeSpaces = False):
        if includeSpaces:
            ll = [[word_tokenize(w), ' '] for w in text.split()]
            return list(itertools.chain(*list(itertools.chain(*ll))))
      
        return word_tokenize(text)

    #Takes the text of string type, returns the list of tuples: (token, list of descriptors)
    def createTableWithDescriptors(self, text):
        paragraphs = self.divideIntoParagraphs(text)
        resultTable = [("",["BTxt"])] #Begining of the text

        #Auxilliary stuff
        rusLetPattern = r"^[а-яА-ЯёЁ]+$"
        latLetPattern = r"^[a-zA-Z]+$"
        dividers = [" ", "*", "=", "\n"]
        numPattern = r"^[0-9]+$"
        spacesPattern = r"\s+"
        smallLettsPattern = r"^[a-zа-яё]+$"
        bigLettsPattern = r"^[A-ZА-ЯЁ]+$"
        floatPattern = r"^\d+\.\d+$"

        #Adding descriptors
        for para in paragraphs:
            sentences = self.divideIntoSentences(para)

            for j in range(len(sentences)):
                words = self.divideIntoWords(sentences[j], True)

                for i in range(len(words)):
                    descripList = []

                    if re.search(rusLetPattern, words[i]):
                        descripList.append("OLE")
                    if re.search(latLetPattern, words[i]):
                        descripList.append("OILE")
                    if words[i] in dividers:
                        descripList.append("ODel")
                    if words[i] in string.punctuation:
                        descripList.append("OPun")
                    if re.search(numPattern, words[i]):
                        descripList.append("ODg")
                    if words[i].isalnum() and self.contatinsLetter(words[i]) and self.containsDigit(words[i]):
                        descripList.append("ODgCh")
                    if len(descripList) == 0:
                        descripList.append("OUnk")
            
                    #Varieties of dividers
                    if re.search(spacesPattern, words[i]):
                        descripList.append("OSpc")
                    if words[i] == "§":
                        descripList.append("OParagraph")

                    #Varieties of punctuation marks
                    if words[i] == "(" or words[i] == "[" or words[i] == "{":
                        descripList.append("OOpn")
                    if words[i] == ")" or words[i] == "]" or words[i] == "}":
                        descripList.append("OCls")
                    if words[i] == "-":
                        descripList.append("OHyp")

                    #Varieties of both punct and dividers
                    if self.consistsOfSameSymbs(words[i]): 
                        if len(words[i]) > 20:
                            descripList.append("OLongDelimSeq")
                        if len(words[i]) > 1:
                            descripList.append("Oplu")
            
                    #Varities of both OLE and OILE descriptos
                    if re.search(smallLettsPattern, words[i]):
                        descripList.append("OLw")
                    if re.search(bigLettsPattern, words[i][0]) and len(words[i]) > 1 and re.search(smallLettsPattern, words[i][1:]):
                        descripList.append("OUpLw")
                    if re.search(bigLettsPattern, words[i]):
                        descripList.append("OUp")

                    #Context descriptors
                    if words[i] == ";":
                        descripList.append("OEOP")
                    if "OUpLw" in descripList and i > 0 and words[i-1] not in ".!?":
                        descripList.append("ONam")
                    if j == 0 and i == 0:
                        descripList.append("OPar")
                    if re.search(floatPattern, words[i]):
                        descripList.append("OFloat1")
                    if words[i] == " " and i > 0 and re.search(floatPattern, words[i-1]):
                        descripList.append("OFloat2")

                    #Paste the word with its descriptors into the result list
                    resultTable.append((words[i], descripList))

        return resultTable

    #Takes the text of string type, returns the list of sentences. Each sentence is a list of words
    def divideIntoSentsAndWords(self, text):
        graphAnResult = []

        #Разбиваем текст на предложения
        sentences = sent_tokenize(text)
        #Разбиваем каждое предложение на слова
        for sent in sentences:
            #Добавляем разделенное на слова предложение в результирующий список
            graphAnResult.append(word_tokenize(sent))

        return graphAnResult

#=======================================Auxillary methods====================================
    def consistsOfSameSymbs(self, word):
        if len(word) <= 1:
            return True
        firstChar = word[0]
        for char in word:
            if char != firstChar:
                return False
        return True

    def contatinsLetter(self, word):
        for letter in word:
            if letter.isalpha():
                return True
        return False

    def containsDigit(self, word):
        for letter in word:
            if letter.isdigit():
                return True
        return False