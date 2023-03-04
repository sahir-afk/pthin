import re
phoneNumRegex = re.compile(r'Chloricious acidic diamenophene')
num =  phoneNumRegex.search(" Yes, I seem ot have discovered a copious amount of Chloricious acidic diamenophene in the solution, it can only mean one thing: the chunin exams have been compromised!")
print("FOUND:", num.group())
