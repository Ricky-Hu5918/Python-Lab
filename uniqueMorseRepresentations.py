#Leetcode.num = 804
import collections

class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse_dic = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.","g":"--.", "h":"....", "i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.", "q":"--.-","r":".-.",'s':"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-", "y":"-.--", "z":"--.."}

        if (len(words) == 0):
            return len(words)
            
        morse_words = []
        for each in words: #将每个单词转换为Morse码
            str1 = ''
            for x in each:
                str1 += morse_dic[x]
            morse_words.append(str1)
        
        #将Morse码去重    
        j = 0
        ll = len(morse_words)
        while (j <= ll):  #此处的“等于”非常重要，不然会出现少一次去重的情况
            for y in morse_words:
                if (morse_words.count(y) > 1):
                    for i in range(1, morse_words.count(y)):
                        morse_words.remove(y)
                        j += 1
            j += len(morse_words) #删除数量加上剩余的数量应该等于最初的总长度

        return len(morse_words)


    '''#aonther way to address this problem'''
    def uniqueMorseRepresentations2(self, words) -> int:
        morse_dic = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.","g":"--.", "h":"....", "i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.", "q":"--.-","r":".-.",'s':"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-", "y":"-.--", "z":"--.."}

        morse_words = set()  #利用集合元素的去重性
        for each in words:
            str1 = ''
            for x in each:
                str1 += morse_dic[x]
            morse_words.add(str1)
        
        return len(morse_words)


    def uniqueMorseRepresentations3(self, words) -> int:
        mapMorse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                    ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_words = []

        for each in words:
            tmp = ''
            for ch in each:
                tmp += mapMorse[ord(ch) - 97]
            morse_words.append(tmp)

        return len(collections.Counter(morse_words).keys())

test = Solution()
words = ["gin", "zen", "gig", "msg"]
print(test.uniqueMorseRepresentations(words), test.uniqueMorseRepresentations2(words), test.uniqueMorseRepresentations3(words))