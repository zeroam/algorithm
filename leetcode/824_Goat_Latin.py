class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        
        goat_words = []
        for i, word in enumerate(words):
            goat_word = ""
            if word[0].lower() in ["a", "e", "i", "o", "u"]:
                goat_words.append(word + "maa" + "a" * i)
            else:
                goat_words.append(word[1:] + word[0] + "maa" + "a" * i)
                
        return " ".join(goat_words)
    

if __name__ == "__main__":
    s = Solution()

    case1 = "I speak Goat Latin"
    expect1 = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert s.toGoatLatin(case1) == expect1

    case2 = "The quick brown fox jumped over the lazy dog"
    expect2 = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    assert s.toGoatLatin(case2) == expect2
