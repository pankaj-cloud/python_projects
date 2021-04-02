import random
main_words = ['yahoo', 'american', 'express']

chosen_word = random.choice(main_words)
print(chosen_word)

display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("please guess a letter : ").lower()
    for position in range(word_lenght):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You Win ! ")