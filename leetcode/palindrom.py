class solution:
    def palindrome(self,x:int)->bool:
        str_x = str(x)
        reversed_str = str_x[::-1]
        print("str_x",str_x)
        print("reversed_str",reversed_str)
        if str_x == reversed_str:
            return True
        else:
            return False    


palindrome_class = solution()
palindrome_def = palindrome_class.palindrome(x=-121)
print("palindrome_def",palindrome_def)



# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 