from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        s_list = list(secret)
        g_list = list(guess)
        index = 0
        while index < len(s_list):
            if s_list[index] == g_list[index]:
                bulls += 1
                s_list.pop(index)
                g_list.pop(index)
            else:
                index += 1
                
                
        index = 0
        while index < len(s_list):
            if s_list[index] in g_list:
                cows += 1

                value = s_list.pop(index)
                g_list.remove(value)
            else:
                index += 1
                    
        return f"{bulls}A{cows}B"


class Solution1:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        s_hash = Counter(secret)

        for idx, ch in enumerate(guess):
            if ch in s_hash:
                if secret[idx] == guess[idx]:
                    cows += 1
                    bulls -= int(s_hash[ch] <= 0)
                else:
                    bulls += int(s_hash[ch] > 0)

                s_hash[ch] -= 1

        return f"{cows}A{bulls}B"


if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()

    secret = "1807"
    guess = "7810"
    expect = "1A3B"
    assert s.getHint(secret, guess) == expect
    assert s1.getHint(secret, guess) == expect

    secret = "1123"
    guess = "0111"
    expect = "1A1B"
    assert s.getHint(secret, guess) == expect
    assert s1.getHint(secret, guess) == expect
