def palindrome(word):
    reverse = word[::-1]
    if(word == reverse):
        return True
    else:
        return False

def anagram(w, w2):
       w = w.lower()
       w2 = w2.lower()
       return sorted(w) == sorted(w2)

print(anagram("icemaN", "Cinema"))

def character_count(word):
    char_dict = {}
    for char in word:
        if(char in char_dict):
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)

character_count("jabiliguns")

def beer(t):
    if t < 1:
        print("""No more bottles of beer on the wall
        No more bottles of beer! """)
        return
    oldt = t
    t -= 1
    print("""{} bottles of beer on the wall
     {} bottles of beeeeer
      take one down, pass it around
       {} bottles of beer on the wall! """.format(oldt, oldt, t))
    beer(t)
beer(10)   