import stddraw
import picture
"""
heady = picture.Picture('narutohead.PNG')
stddraw.picture(heady, -2,6)
"""
stddraw.setCanvasSize(400, 400)
stddraw.setXscale(-10,10)
stddraw.setYscale(-10,10)
stddraw.show(500)

stddraw.setPenColor(stddraw.BLACK)
stddraw.filledSquare(0.0,0.0,10)

def Head(guess):
    if guess <= 7:
        stddraw.setPenRadius(0.09 * 400 / ((10 - -10) * 256))
        stddraw.circle(-2, 6, 2.0)
        stddraw.show(100)

def Torso(guess):
    if guess <= 6:
        stddraw.setPenRadius(0.1)
        stddraw.line(-2, 4, -2, -4)
        stddraw.show(100)

def left_arm(guess):
    if guess <= 5:
        stddraw.line(-2, 2, -4, -2)
        stddraw.show(100)

def right_arm(guess):
    if guess <= 4:
        stddraw.line(-2,2, 0, -2)
        stddraw.show(100)

def right_leg(guess):
    if guess <= 3:
        stddraw.line(-2, -4, -4, -6)
        stddraw.show(100)

def left_leg(guess):
    if guess <= 2:
        stddraw.line(-2, -4, 0, -6)
        stddraw.show(100)

def H_thing(guess):
    if guess <= 1:
        stddraw.line(-10,-9,10,-9)
        stddraw.line(-9, -9, -9, -8)
        stddraw.line(9, -9, 9, -8)
        stddraw.line(-9, -8, 9, -8)
        stddraw.line(7,-8, 7,9)
        stddraw.line(7,9, -2, 9)
        stddraw.line(-2, 9, -2, 8)
        stddraw.show(1000)

def face(guess):
    if guess == 0:
        stddraw.line(-1, 7, -2, 6)
        stddraw.line(-1, 5.5, -2, 6)
        stddraw.line(-2.5, 6, -3.5, 5.5)
        stddraw.line(-2.5, 6, -3.5, 7)
        stddraw.line(-2.9, 4.8, -2.5, 5.2)
        stddraw.line(-2.5, 5.2, -2.1, 4.8)
        stddraw.line(-2.1, 4.8, -1.7, 5.2)
        stddraw.line(-1.7, 5.2, -1.3, 4.8)
        stddraw.show(4000)

def start_draw(guess, guessed, blank_array):
    Wguess(guessed)
    Rguess(blank_array)
    stddraw.setPenColor(stddraw.WHITE)
    Head(guess)
    Torso(guess)
    left_arm(guess)
    right_arm(guess)
    right_leg(guess)
    left_leg(guess)
    H_thing(guess)
    face(guess)




def Wguess(guessed):
    stddraw.setFontSize(22)
    stddraw.setPenColor(stddraw.GRAY)
    stddraw.text(3,5, "Wrong Guesses:")
    stddraw.setFontSize(30)
    stddraw.setPenColor(stddraw.PINK)
    for i in range(len(guessed)):
        stddraw.text(i ,4,''.join(guessed[i]))
    stddraw.show(500)

def Rguess(blank_array):
    stddraw.setFontSize(30)
    stddraw.setPenColor(stddraw.GREEN)
    for i in range(len(blank_array)):
        stddraw.text(i - 5,-8.5, ''.join(blank_array[i]))
    stddraw.show(500)

def win(chosen_word):
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledSquare(0.0,0.0,10)
    stddraw.setFontSize(70)
    stddraw.setPenColor(stddraw.MAGENTA)
    stddraw.text(0.0, 0.0, "YOU WIN xD")
    stddraw.setFontSize(30)
    stddraw.text(0.0, -4, "The word was: ")
    stddraw.text(0.0, -5, str(''.join(chosen_word)))
    stddraw.show(9000)

def lose(chosen_word):
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledSquare(0.0,0.0,10)
    stddraw.setFontSize(70)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.text(0.0, 0.0, "Oops :(")
    stddraw.setFontSize(30)
    stddraw.text(0.0, -4, "You couldn't guess the word!")
    stddraw.text(0.0, -5, "The word was: ")
    stddraw.text(0.0, -6, str(''.join(chosen_word)))
    stddraw.show(9000)
