import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
num =  phoneNumRegex.search(" Yes, I seem ot have discovered a copious amount of 651-432-0382 in the solution, it can only mean one thing: the chunin exams have been compromised!")
print("FOUND:", num.groups())
area_code, main_num = num.groups()
print(area_code)