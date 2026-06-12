class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr = ""

        for word in strs:
            enstr += str(len(word)) + "#" + word

        return enstr

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            word = s[start : start + length]

            result.append(word)

            i = start + length

        return result
        




