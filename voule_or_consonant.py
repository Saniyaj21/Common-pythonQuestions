text = input("Enter a alphabet to check voule or consonant : ")

voule = ["a", "e", "i", "o", "u"]
if text.lower() in voule:
    print("Alphabet is voule :")
else:
    print("Alphabet is not voule :")
