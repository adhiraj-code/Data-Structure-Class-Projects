# function to check whether palindrome or not

r = (1, 2, 3, 3, 2, 1)

def palindrome(r):

    e = len(r) - 1

    s = 0

    while s < e:

        if r[s] != r[e]:

            return False

        s += 1

        e -= 1

    return True

if palindrome(r):

    print("The Tuple is palindrome")

else:

    print("The Tuple is not palindrome")