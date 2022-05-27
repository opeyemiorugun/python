# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open(filename,"r")
    new_file = file.read()
    return new_file


def count_words():
    text = read_file_content("story.txt")
    words = text.split()
    dict = {}

    
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

print(count_words())
    