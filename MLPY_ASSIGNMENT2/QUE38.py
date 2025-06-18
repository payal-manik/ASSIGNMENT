# Write a function that checks if a sentence is a pangram. 

def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(sentence.lower())
    return len(alphabet - letters) == 0


print(is_pangram("Pack my box with five dozen liquor jugs"))  
print(is_pangram("Hello world"))                                
