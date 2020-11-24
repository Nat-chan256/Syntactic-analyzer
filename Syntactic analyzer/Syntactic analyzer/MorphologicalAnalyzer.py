from pymorphy2 import MorphAnalyzer

class MorphologicalAnalyzer:

    def analyzeWord(self, word):
        morph = MorphAnalyzer()

        p = morph.parse(word)[0]

        result = {
                'исходное слово': word,
                'нормальная форма': p.normal_form,
                'часть речи': p.tag.POS,
                'одушевленность': p.tag.animacy,
                'вид': p.tag.aspect,
                'падеж': p.tag.case,
                'род': p.tag.gender,
                'включенность': p.tag.involvement,
                'наклонение': p.tag.mood,
                'число': p.tag.number,
                'лицо': p.tag.person,
                'время': p.tag.tense,
                'переходность': p.tag.transitivity,
                'залог': p.tag.voice,
                'лексема': [lexeme[0] for lexeme in p.lexeme]
            }

        return result
