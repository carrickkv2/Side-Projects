'''Is a palindrome

Ask the user to give you five words. Then check if any of the five words is a palindrome.

A palindrome is a word that remains the same whether it's read forward or backward.

Example:

    madam is a palindrome.
    so is malayalam.
    But not geeks.
'''
'''
Pseudocode

1) Create a function
2) Ask the user for input (5 words)
3) For all of the inputs the user gives, check if any of them are palidromes
'''

if __name__ == '__main__':

    list = list()

    def is_palindrome(n=5): #create the function
        """Checks if a word is a palindrome"""
        for number in range(n):
            text = input()
            if text[::] == text[::-1]:
                list.append(text)



is_palindrome()
print(list)
