import sys
import random
import hangman_game as hang

words = open(sys.argv[1], 'r').readlines()
word = []
long_word = []
chosen_word = []
blank_array = []
guessed = []
guess = 8
Guess_len = 0

def append(word):
	for num in words:
		word.append(num.strip())
	return word


def choose(word):
	for i in range(len(word)):
		if len(word[i]) >= 4:
			long_word.append(word[i])
	a = random.randint(0, len(long_word))
	chosen_word.append(long_word[a])
	for i in range(len(chosen_word[0])):
		blank_array.append('_')
	return chosen_word


def say(blank_array, guess):
	print('')
	print("The Secret word looks like:", ''.join(blank_array))
	print("You have", guess,"wrong guesses left")
	if guess != 8:
		print ("Bad guesses so far:", ' '.join(guessed))


def guesstime(chosen_word, guessed, guess):
    say(blank_array, guess)
    Gword = input("What's your next guess? ")
    for index, num in enumerate(chosen_word[0]):
        if Gword == num:
            blank_array[index] = num

    if Gword in blank_array:
        print("Nice Guess!")

    elif Gword in guessed:
        print("Sorry this word has already been guessed, Please try again")

    else:
        guessed.append(Gword)
        print("sorry, there is no '", Gword, "'")


print("Hello! Welcome to CPSC 231 Console Hangman!")
append(word)
choose(word)
while guess != 0:
    hang.start_draw(guess, guessed, blank_array)
    guesstime(chosen_word, guessed, guess)
    if len(guessed) != Guess_len:
        guess -= 1
        Guess_len += 1
    if '_' not in blank_array:
        print("Congrats! You found the word!, it was '", ''.join(blank_array), "'")
        hang.win(chosen_word)
        break
    elif guess == 0:
        print("You couldnt guess the word! YOU LOSE")
        print("The word was '",''.join(chosen_word),"'")
        hang.lose(chosen_word)
        break
