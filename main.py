# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        content= f.read()

    return content


def count_words():
    # [assignment] Add your code here
    text = read_file_content('./story.txt')
    
    counted_words = { }
    for word in set(text.split()):
        counted_words[word] = text.split().count(word)
    return (print(counted_words))
    
count_words()

