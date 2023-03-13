

def longest_palindromic_subsequence(word):
    # returns the length of the palindrome as well as the lps itself.
    i = 0
    n = len(word)
    lhlps = ""
    rhlps = ""
    middle = ""
    recent = (None, None)

    while i <= n:
        for c in reversed(range(i+1,n)):
            if word[i] == word[c]:
                lhlps += word[i]
                rhlps = word[c] + rhlps
                n = c
                recent = (i, c)
                break
        i += 1

    if (c-1) not in recent:
        middle += word[c-1]

    lps = lhlps + middle + rhlps

    return len(lps), lps

def main():
    word = 'aibohphobia'
    len, palindrome = longest_palindromic_subsequence(word)

    print(len)
    print(palindrome)


if __name__ == '__main__':
    main()
