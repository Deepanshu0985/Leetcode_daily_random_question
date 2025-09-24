class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = []
        if numerator < 0 and denominator>0:
            ans.append("-")
        elif numerator > 0 and denominator<0:
            ans.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        num = numerator % denominator 
        ans.append(str(numerator//denominator))
        if num == 0:
            return ''.join(ans)
        ans.append('.')
        
        freq = {}
        while num != 0:


            num *= 10
            digit = num // denominator
            ans.append(str(digit))    
            num = num % denominator

            if num in freq:
                idx = freq[num]
                ans.insert(idx, "(")
                ans.append(")")
                return "".join(ans)

            freq[num] = len(ans)
        return "".join(ans)
                