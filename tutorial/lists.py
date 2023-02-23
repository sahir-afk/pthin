while(True):
    best_players = ('Federer', 'Nadal', 'Djokovic', 'Sampras', 'Rune', 'Alcaraz', 'Kyrgios', 'Roddick')
    guess = input("Who do you think is the best tennis player of all time? ")
    if guess in best_players:
        print("Good choice! ", guess, " is a very good player, and I would say that he is one of the best of all time.")
    elif guess not in best_players:
        print("bruh... ", guess," kinda sucks.")