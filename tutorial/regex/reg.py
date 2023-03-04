import re
phoneNumRegex = re.compile(r'(\d\d\d)?-?(\d\d\d-\d\d\d\d)')
num =  phoneNumRegex.search(" Yes, I seem ot have discovered a copious amount of 651-432-0382 in the solution, it can only mean one thing: the chunin exams have been compromised!")
num2 = phoneNumRegex.search("My numba is 876-2873")
print(num2.group())

print("FOUND:", num.groups())
area_code, main_num = num.groups()
print(area_code)

batman = re.compile(r"Bat((wo)*man|mobile|arang|wing|copter)")
bat1 = batman.search('Batwowowowoman exploded!!')
print(bat1.group())

batman2 = re.compile(r"Bat((wo)+man|mobile|arang|wing|copter)")
bat2 = batman2.search('Batwoman exploded!!')
print(bat2.group())

laughRegex = re.compile(r'(ha){2,4}')
lol = laughRegex.search("hahaha")
print(lol.group())