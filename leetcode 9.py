class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        def isPali_2digit(x):
            if (x/10) == (x%10):
                return True
            else:
                return False

        if x == 0:
            return True
        if x < 0 or x%10 == 0:
            return False
        if x < 10:
            return True
        else:
            if x < 100:
                return isPali_2digit(x)
            else:
                num_length = 0
                num = x
                while num>0:
                    num /= 10
                    num_length += 1
                    
                if num_length % 2 == 1:
                    x = x/(10**(num_length/2+1))*(10**(num_length/2))+x%(10**(num_length/2))
                    return self.isPalindrome(x)
                else:
                    if x%(10**(num_length/2+1))/(10**(num_length/2-1)) == 0:
                        x = x/(10**(num_length/2+1))*(10**(num_length/2-1))+x%(10**(num_length/2-1))
                        return self.isPalindrome(x)
                    elif x%(10**(num_length/2+1))/(10**(num_length/2-1)) <= 10:
                        return False
                    else:
                        if isPali_2digit(x%(10**(num_length/2+1))/(10**(num_length/2-1))):
                            x = x/(10**(num_length/2+1))*(10**(num_length/2-1))+x%(10**(num_length/2-1))
                            return self.isPalindrome(x)
                        else:
                            return False

a = Solution()
print Solution.isPalindrome(a, 100021)