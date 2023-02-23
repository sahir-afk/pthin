import random
c =  ["gaga", "googoo", "jobin", "bagin", "e9ufbiu"]
d = [6, 7, 8, 4]
e = [12, 342, 545, 8]
b = []
for i, item in enumerate(c):
    print(c[i], i)
    

for i in range(25,51):
    print(i)

for i, item in enumerate(d):
    b.append(d[i] * e[i])
print(b)

print("enter 0 to quit")
# while True:
#     x = random.randint(1, 101)
    
#     sopa = (input("Pick an integer from 1 to 100 "))

#     try:
#         sopa = int(sopa)
#     except ValueError:
#         print("Enter an integer dumbo")
#         continue
        
#     if(sopa == x):
#         print("Thats right! ")
#         break
#     elif(sopa == 0):
#         print("hahahahah loser!!!")
#         break
#     else:
#         print("*buzzer noise* WROOONNNNGGG")
