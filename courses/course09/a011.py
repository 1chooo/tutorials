"""
Created Date: 2023-11-25
Author: @1chooo (Hugo ChunHo Lin)
Problem link: https://zerojudge.tw/ShowProblem?problemid=j605
Status: AC
"""

while 1:  # Continuous loop until broken
    try:
        n = 0  # Counter for word endings
        s = input()  # Take input from user

        # Loop through each character in the input string except the last character
        for i in range(len(s) - 1):
            # Check if the current character is an alphabet character and the next character is not an alphabet character
            if s[i].isalpha() and not s[i + 1].isalpha():
                n += 1  # Increment the counter when an alphabet character is followed by a non-alphabet character

        # Check the special case where the second last character is not an alphabet character and the last character is an alphabet character
        if not s[-2].isalpha() and s[-1].isalpha():
            n += 1  # Increment the counter for this special case

        print(n)  # Print the total count of word endings
    except:  # Catch any exceptions to break out of the loop
        break
