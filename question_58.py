# question - 58 (Length of Last Word) [EASY] result = 100%

def lengthOfLastWord(s):
    # print(f"The last word is \"{s.split()[-1]}\" with length {len(s.split()[-1])}.")
    return len(s.split()[-1])


# Example usage
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("a"))
