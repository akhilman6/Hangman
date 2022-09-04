import random
import hangman_word
import hangman_art

print(hangman_art.logo)

rndm = random.choice(hangman_word.word_list).lower()
#print(rndm)
length = len(rndm)
list = []
for l in range(length):
    list += "_"
print(list)
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(0, length):
        if guess in list[i]:
            print(f'You already guessed {guess}. Guess another letter.')
            break
        if guess == rndm[i]:
            list[i] = guess
    print(list)
    if guess not in rndm:
        lives -= 1
        print(f'Your guess {guess} is wrong. You lose a life.')
    print(hangman_art.stages[lives])
    if "_" not in list:
        end_of_game = True
        print("You Win!!!")
    if lives == 0:
        end_of_game = True
        print("You lose!!")
        print(f'The word is {rndm}.')
