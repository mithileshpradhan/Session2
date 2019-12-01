def longestWord(words):
    max_length = 0
    for word in words:
        currentLength = len(word)
        if currentLength > max_length:
            max_length = currentLength
            target_word = word

    
    return target_word


print(longestWord(["Good","Bad","Excellent","Poor","Outstanding"]))

