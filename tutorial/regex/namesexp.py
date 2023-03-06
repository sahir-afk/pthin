import re
first = input("what is your first name? ")
last = input("what is your last name? ")
invalid_reg_ex = re.compile(r"[^a-zA-Z\s]+")
invalid = invalid_reg_ex.findall("{} {}".format(first, last))
invalod = True
if len(invalid) > 1:
    invalod = False

print(invalid, invalod)