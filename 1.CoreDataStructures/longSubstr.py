"""

Longest Substring Without Repeating Characters -
Find the length of the longest substring without
repeating characters.

"""

def longSubstr(string):
    max_ = 0
    seen = set()
    left = 0
    for right in range(len(string)):
        while string[right] in seen:
            seen.remove(string[left])
            left += 1

        seen.add(string[right])
        max_ = max(max_, right-left+1)
    return max_

str_ = "abcdeabcxyxabcdesfg"
print(longSubstr(str_))

