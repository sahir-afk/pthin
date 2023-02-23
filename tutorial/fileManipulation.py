import os, csv

os.path.join("C:", "Users", "sahir", "pthin", "manipulated_file.txt")
os.path.join("C:","sers","sahir","Videos",".gallery","165c9eb0-bf0e-4152-9870-bc6156ba5941","Info.txt")
manipulated_file = open("manipulated_file.txt", "w+")
manipulated_file.write("nothing is at is it seems")
manipulated_file.close()

movies_list = [["Top Gun", "Top Gun Maverick"], ["Cars", "Megamind"], ["Incredibles", "Bolt"]]


answer = input("What is your philosophy? ")

with open("manipulador.txt", "w+") as manipulador:
    manipulador.write(answer)

with open("reader_file", "r") as filo:
    print(filo.read())

with open("cyka.csv", "w+", newline='') as cyka:
    cuka = csv.writer(cyka, delimiter=",")
    cuka.writerow([1, 2, 3, 4, 5, 6 , 7, 7.5])
    cuka.writerow([1, 2, 3, 4, 5, 6, 7, 7.5])

with open("movies.csv", "w+", newline ='') as movies:
    movie = csv.writer(movies, delimiter=",")
    for i in movies_list:
        movie.writerow(i)
