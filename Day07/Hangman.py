import random

# Hangman stages
stages = [
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |      / \\
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |      / 
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |       |
      |
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |
      |
      |
    __|___
    """,
    """
       _______
      |/      |
      |
      |
      |
      |
    __|___
    """
]

word_list = ['aardvark','baboon','camel']
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Enter a guess: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # Wrong guess → decrease life & show hangman
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])     # show hangman image
        if lives == 0:
            game_over = True
            print("You Lose")

    # Win if no underscores
    if "_" not in display:
        game_over = True
        print("You win!")
