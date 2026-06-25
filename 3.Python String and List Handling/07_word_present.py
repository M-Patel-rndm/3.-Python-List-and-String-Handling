sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word Found")
else:
    print("Word Not Found")