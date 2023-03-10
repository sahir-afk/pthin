import re
phoneNumRegex = re.compile(r'(\d\d\d)?-?(\d\d\d-\d\d\d\d)')
phoneNumRegex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
num =  phoneNumRegex.search(" Yes, I seem ot have discovered a copious amount of 651-432-0382 in the solution, it can only mean one thing: call 726-738-3287 as the chunin exams have been compromised!")
num2 = phoneNumRegex.search("My numba is 876-2873, ")
num3 = phoneNumRegex2.findall("Yes, I seem ot have discovered a copious amount of 651-432-0382 in the solution, it can only mean one thing: call 726-738-3287 as the chunin exams have been compromised!")
print(num2.group())
print(num3)

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
lol = laughRegex.search("hahahahahahahhah")
print(lol.group())

laughRegex2 = re.compile(r'(ha){2,4}?')
lol2 = laughRegex.search("hahahahahaha")
print(lol2.group())

vowelRegex = re.compile(r"[AEIOUaeiou]")
crazy = vowelRegex.findall("a  e  a  i  o auwd design of the bad portable light switch yiedkowski point eight nine five sixteen pigs in a cage with protons on either side")
print(crazy)

vowelRegex2 = re.compile(r"[^AEIOUaeiou]")
crazy2 = vowelRegex2.findall("a  e  a  i  o auwd design of the bad portable light switch yiedkowski point eight nine five sixteen pigs in a cage with protons on either side")
print(crazy2)

date_reg_ex = re.compile(r"""
([0-2]\d|3[01])     #day
(\s|.|/|-)          #dash
(0\d|1[12])         #month first
(\s|.|/|-)          #dash
([1-2]\d{3})        #year

""", re.VERBOSE)
dormamu = input("enter the date: ")
date = date_reg_ex.findall(dormamu)
for num in date:
    year = int(num[4])
    month = int(num[2])
    day = int(num[0])
    if(year % 4 != 0 or year % 100 == 0 and month == 2 and day > 28 and year % 400 != 0):
        print("invalid date")
    elif(month == 2 and day > 29):
        print("invalid date")
    else:
        print("".join(num))
        
    


