# question - 3 (longest substring without repeating characters)
# runtime - 167 ms and beats 93.42%

def lengthOfLongestSubstring(s):
    past = ""
    current = ""
    for i in s:
        if i not in current:
            current += i
        else:
            if current.find(i) >= 0:
                # new_current = ""
                # for j in range(current.find(i) + 1, len(current)):
                #     new_current += current[j]
                new_current = current[current.find(i)+1:]
                new_current += i
                if len(past) < len(current):
                    past = current
                current = new_current
            elif len(past) < len(current):
                past = current
                current = i

    # print("past:\t\t" +past)
    # print("current:\t"+current)

    if len(past) > len(current):
        print("answer is past string: " + s + " = " + past)
        return len(past)
    print("answer is current string: " + s + " = " + current)
    return len(current)


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")
lengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring("1R1TS")
lengthOfLongestSubstring("7stsUB")
