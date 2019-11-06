import sys
import random
#import graphics

input_file = open(sys.argv[1])
lines = input_file.readlines()
input_file.close()

just_words=[]
for i in range(len(lines)):
    words = lines[i].rstrip()
    just_words.append(words)
#print(just_words)

word = random.choice(just_words)
underscore = '_'*len(word)
secret = word.replace(str(word), underscore)
print(word)
#random secret word with at least four letters
if len(word) >= 4:
    print('Your secret word looks like:', secret)



letters = list(word) #separates each letter and puts in a list
print(letters)
blanks = list(underscore)
print(blanks)

#Successive letter guessing
guesses_left = 8
bad_guesses = []
while guesses_left > 0:
    guess = input("What's your next guess? ")
    for underscore in blanks:
        if guess in word:
            for i in range(len(letters)):
                if letters[i] == guess:
                    blanks[i] = letters[i]
                    swap = blanks
            position = letters.index(guess) #find index of the letter guess
            letter_in_position = letters[int(position)] #the letter!!#uses position number and make into letter again
            blanks[position] = letter_in_position #replacement of underscore to a letter
            print('Your secret word looks like: ', "".join(blanks)) #change list back to string
            print('Nice guess!', '\n')
            break
        elif guess not in word:
            #put bad guesses in empty array and keep printing them after each turn
            if guess not in bad_guesses:
                #graphics.start_draw(guesses_left)
                bad_guesses += guess
                print('Sorry, there is no','"', guess,'".')
                print('Your bad guesses so far: ', "".join(bad_guesses))
                guesses_left -= 1
                print('You have', guesses_left, 'remaining.\n')
            elif guess in bad_guesses:
                print('Letter has already been guessed before, please try again.\n')
            break

    if guesses_left == 0:
        #graphics.start_draw(guesses_left)
        print("You lose. The word was:", word, '\n')
        break
    if "_" not in blanks:   #no underscores/blanks left
        print('Congratulations!\nYou guessed the secret word:', word, '\n')
        break
