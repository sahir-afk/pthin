def fizzbuzz(x):
    for i in range(1, x):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        if(i % 5 == 0):
            print("Buzz")
        if(i % 3 == 0):
           print("Fizz")
        else:
            print(i)

def palindrome(word):
    word.lower()
    if(word[::-1] == word):
        return True
    else:
        return False
    
print(palindrome("jojojojoj"))