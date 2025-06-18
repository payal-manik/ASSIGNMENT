#  Create a function that accepts a string and returns a dictionary of word counts. 

def word_count(text):
    words = text.split()     
    counts = {}               

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


sentence = "hello world hello"
print(word_count(sentence))
