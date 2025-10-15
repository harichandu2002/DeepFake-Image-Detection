def anagram(w1,w2):
    w1=sorted(w1)
    w2=sorted(w2)
    if w1==w2:
        return "They are anagrams"
    else:
        return "They are not anagrams"
    
w1 = list(input("Enter word 1: ").lower())
w2 = list(input("Enter word 2: ").lower())
print(anagram(w1,w2))

