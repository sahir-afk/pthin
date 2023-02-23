favorite_songs = ['Hotel California', "House of the Rising Sun", "Skyfall", "Good Riddance", "Holiday", "American Idiot"]

facts_about_me = {"favorite runner" : "Hicham el Guerrouj",
"favorite movie" : "Megamind/Cars",
"age" : "16",
"height" : "5'10''",
"sports" : "tennis and running",
"favorite subject in school": "Math/Compsci",
"favorite color" : "Red/Dark Navy Blue",
"favorite songs" : favorite_songs}

question = input("What fun fact do you want to know about me? ")

if question in facts_about_me:
    print(facts_about_me[question])
else:
    print("Your clearance level is too low for you to access that information, ask me something else.")