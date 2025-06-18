#  Create a function that accepts a sentence and returns the longest word.

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest


sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(sentence))
