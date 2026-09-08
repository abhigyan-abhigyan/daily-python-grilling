# Given an integer n, return True if it is a power of two. Otherwise, return False.
# An integer n is a power of two if there exists an integer x such that n == 2^x (solved using recursion).

def isPowerOfTwo(self, n):
        if n <= 0:
         return False
        if n == 1:
         return True
        
        if n%2==0:
            n = n//2
            self.isPowerOfTwo(n)
            return True
        else:
            return False   