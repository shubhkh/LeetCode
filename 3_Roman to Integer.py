from PIL.TiffTags import lookup


class Solution:
    def romanToint(self,s:str):
        lookup={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        N = len(s)
        i=N-1
        output=0
        while i>=0:
            if i< N-1 and lookup[s[i]] < lookup[s[i+1]]:
                output=output-lookup[s[i]]

            else:
                output=output+lookup[s[i]]
            i=i-1

        return output

