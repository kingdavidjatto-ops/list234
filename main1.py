def match_words(words):
    result = []


    for word in words:
        if len(words) >1 and word[0] == word[-1]:
            result.append(word)

    print("list of words with first and last character same:  ", result)
    return len(result)

count = match_words(['abc','cfc','zyz','kfc','defg'])

print("Number of words having first and last character same:  ",count)