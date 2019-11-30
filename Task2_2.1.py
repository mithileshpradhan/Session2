def word2int(words):
    listofint = [len(word) for word in words]
    return listofint


print("List of integers is ",word2int(["Good","Bad","Excellent","Poor","Outstanding"]))