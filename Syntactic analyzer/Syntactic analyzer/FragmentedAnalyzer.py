from enum import Enum


class FragmentedAnalyzer:

    #Takes the list of sentences, where each sentences is represented as a list of words
    def analyzeText(text):


#==============================Auxilary classes========================
    class FragmentType(Enum):
        VERB = 1 #Verb
        PRTS = 2 #Short participle
        ADJS = 3 #Short adjective
        PRED = 4 #Predicative
        PRTF = 5 #Full participle
        GRND = 6 #Gerunds
        INFN = 7 #Infinitive
        INTR = 8 #Introductory word
        NONE = 9 #None of above


    class Fragment:
        type = FragmentType.NONE
