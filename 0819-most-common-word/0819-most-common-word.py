class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        from collections import Counter

        # Supprimer la ponctuation et convertir en minuscules
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()

        # Séparer les mots et compter les occurrences
        word_count = Counter(paragraph.split())

        # Filtrer les mots bannis
        for ban_word in banned:
            word_count.pop(ban_word, None)

        # Trouver le mot le plus courant
        most_common_word = word_count.most_common(1)

        return most_common_word[0][0] if most_common_word else ""
