def vowel_check(mychar):
    vowels = "aeiou"
    if mychar in vowels:
        return "It is a vowel"

    else:
        return "It is not a vowel"


print(vowel_check("e"))