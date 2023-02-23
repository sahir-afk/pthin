sentence = ["cawn", "caiwncanw", "coijawcna", ", ", "cpanfic", "ewirnf", "aofiano", "."]
sentence1 = " ".join(sentence)
sentence1 = sentence1[0: -2] + "."
print(sentence1)
sentence1 = sentence1.replace("c", "s")
m = sentence1.index("w")
sentence1 = sentence1.split(",")
sentence1.pop()
sentence1 = " ".join(sentence1)
print(sentence1)
print(m)