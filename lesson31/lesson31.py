# Lesson 31
def anagram_check(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = input("Enter your word: ")
word2 = input("Enter your second word bro: ")

if anagram_check(word1, word2):
    print("AMOGUS: your word is an anagram!")
else:
    print("Nah it's not!")