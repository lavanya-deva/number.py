def repeatedletter(word):
    h={}
    for ch in word:
        if ch in h:
            return ch;
        else:
            h[ch]=0
print(repeatedletter("lavanya"))
