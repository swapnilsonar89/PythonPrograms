class Solution(object):
    def plusOne(self,digits):
        if len(digits) == 1:
            if digits[0] == 9:
                digits.append(0)
                digits[0] = 1
            else:
                digits[0] += 1
                
        elif digits[-1] == 9:
            l = len(digits)-1
            while l != 0:
                if digits[l] == 9:
                    digits[l] = 0
                    l -= 1
                else:
                    digits[l] += 1
                    break
            if l == 0:
                if digits[l] == 9:
                    digits[l] = 0
                    digits.insert(0,1)
                else:
                    digits[l] += 1
        else:
            digits[-1] += 1
            

        return digits
