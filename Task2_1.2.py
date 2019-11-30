def filter_long_words(words,n):
    filtered_words = []
    for word in words:
        if len(word) > n:
            filtered_words.append(word)

    return filtered_words

print(filter_long_words(["Good","Bad","Excellent","Poor","Outstanding"],6))