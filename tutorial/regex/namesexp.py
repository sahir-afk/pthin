import re
# first = input("what is your first name? ")
# last = input("what is your last name? ")
# invalid_reg_ex = re.compile(r"[^a-zA-Z\s]+")
# invalid = invalid_reg_ex.findall("{} {}".format(first, last))
# invalod = True
# if len(invalid) > 1:
#     invalod = False

# print(invalid, invalod)

secret_agent = re.compile(r"Agent \w+", re.I)
censur = secret_agent.sub("X", "Agent John has disposed of target 27, but unfortunately, agent john was compromised in the altercation")
print(censur)