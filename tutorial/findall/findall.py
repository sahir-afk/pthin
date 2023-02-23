import re

zen = "The ghost that says boo haunts the loo"

m = re.findall(".oo", zen, re.IGNORECASE)

print(m)