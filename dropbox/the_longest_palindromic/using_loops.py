def longest_palindromic(text):
    longest = ''
    for i in range(len(text)):
        for j in range(len(text[i:]), len(longest), -1):
            if text[i:][:j] == text[i:][:j][::-1] and len(longest) < len(text[i:][:j]):
                longest = text[i:][:j]
    return longest
