class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        encodedString = list(s)

        while len(encodedString) > 0:
            wordLengthString = ""
            for i in encodedString:
                if i != "#":
                    wordLengthString += i
                else:
                    break

            wordLengthNum = int(wordLengthString)  

            letters = encodedString[len(wordLengthString)+1:len(wordLengthString)+1+wordLengthNum]   

            word = ""

            for j in letters:
                word += j

            decoded.append(word)

            encodedString = encodedString[len(wordLengthString)+wordLengthNum+1:]

        return decoded