word = input("Enter a word : ")
word = word.lower()
word_reverse = word[::-1] #it will reverse the word

if word == word_reverse:
    print("The word is palindrome.")
else:
    print("The word is not palindrome.")