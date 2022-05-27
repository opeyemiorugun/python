# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True




def find_anagram(word, anagram):
    words = list(word)
    anagrams = list(anagram)
    words.sort()
    anagrams.sort()

    if words == anagrams :
        return True
    else:
        return False

        
        

print(find_anagram("hello", "check"))
print(find_anagram("below","elbow"))
