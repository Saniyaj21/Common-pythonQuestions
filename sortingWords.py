input_word = input("Enter a sentence : ")
input_word.lower()
words = input_word.split()
words.sort()
for i in words:
    print(i)