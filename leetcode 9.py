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

    def isPalindrome2(self, x):
        origin = x
        reverse = 0
        if x<0:
            return False
        else:
            while x>0:
                reverse = x%10 + reverse*10
                x = x/10
            print reverse
            if reverse == origin:
                return True
            else:
                return False