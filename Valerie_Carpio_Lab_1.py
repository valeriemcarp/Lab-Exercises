#Question 1
old_list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
y = old_list[0]

for word in old_list[1:]:
    if len(word) >= len(y):
        y = word

print(y)

#Question 2
from aifc import _aifc_params
import random

with open("all scrabble words ever.txt") as file: 
    allwords = file.read()
    words = list(map(str, allwords.split()))
b = len(words) - 1
a = 0
w = []

for i in range(7):
    w.append(words[random.randint(a,b)])
y = w[0]

for word in w[1:]:
    if len(word) >= len(y):
        y = word

print(y)

#Question 3
fruits_colors = {"apple" : "red", 
                 "banana" : "yellow", 
                 "purple" : "grape"}
new_fruits = fruits_colors.copy()
new_fruits.update({"pomegranate" : "red"})
banana_color = new_fruits.get("banana")
new_fruits.pop("apple")
print(banana_color)
print(new_fruits)

#Question 4
class Student:
    def __init__(self, name):
        self.name = name

    def check_year(self, year):
        self.year = year   
        print("You are in your", self.year, "year.")

    def check_grades(self, A, B, C, D, F):
        self.As = A 
        self.Bs = B
        self.Cs = C
        self.Ds = D
        self.Fs = F
        print("You have", A, "many As.")
        print("You have", B, "many Bs.")
        print("You have", C, "many Cs.")
        print("You have", D, "many Ds.")
        print("You have", F, "many Fs.")

    def convert_grades(self, num):
        self.convert = num
        if num >= 90:
            print("This is an A.")
        elif num >= 80:
            print("This is a B.")
        elif num >= 70:
            print("This is a C.")
        elif num >= 60:
            print("This is a D")
        elif num <= 59:
            print("This is an F")

s1 = Student("Valerie")
s1.check_year("Junior")
s1.check_grades(8, 5, 3, 2, 0)
s1.convert_grades(89)

#Question 5
word = ("grape") #This declares the variable "word" to be the string "grape"
ask = str(input("Would you like to play Hangman? ")) #This sets the variable "ask" to ask the user for input when printing "Would you like to play? ", and then declares that input to be a string
            
guesses = [] #This initializes the variable "guesses" to be an empty list
correct_guesses = [] #This initializes the variable "correct_guesses" to be an empty list
fails = 0 #This initializes the variable "fails" to be equal to the variable 0
game = "" #This initializes the variable "game" to be equal to an empty string
for char in word: #This creates a for loop that iterates through each character in "word"
	game += "_ " #This causes "game" to be added to and then = to "_ ", and with the for loop will print a "_ " for each character in "word"

code_letters = [] #This initializes the variable "code_letters" to be an empty list
for char in word: #This creates a for loop that iterates through each character in "word"
	if char not in code_letters: #This creates a conditional for if a character is not in "code_letters"
		code_letters.append(char) #This adds a character that is not in "code_letters" to it
code_letters.sort() #This sorts the list "code_letters" in ascending order after the for loop

if input == "Yes" or "yes": #This creates a conditional for if the above input from "ask" = "Yes" or "yes"
    print("Guess the word!") #This prints "Guess the word!" if the input meets the conditional requirement
    print(game) #This prints the variable "game" if the input meets the conditional requirement

while (fails < 6): #This creates a while loop for when "fails" are less than 6
	letter = input("Guess a letter: ").lower() #This sets "letter" = to the input for "Guess a letter: ", and sets the variable as lowercase with .lower()
	if letter in guesses: #This creates a conditional for if "letter" is in "guesses"
		print("You already guessed that letter!") #This prints "You already guessed that letter!" if the above conditional is met
	else: #This sets a procedure for if the conditional is false
		guesses.append(letter) #This adds the input that is now equal to "letter" to "guesses"
		guesses.sort() #This then sorts "guesses" after "letter" has been added
		if letter in word: #This sets a condition for if "letter" is in "word"
			correct_guesses.append(letter) #If the condition is met, "letter" will be added to "correct_guesses"
			correct_guesses.sort() #If the condition is met, "correct_guesses" will be sorted after "letter" was added
			for i in range(len(word)): #This creates a for loop to iterate through each item in the specific range, which in this instance is the length of "word"
				if word[i] == letter: #This creates a conditional for if the item in "word" is also equal to "letter"
					copy = list(game) #This creates a variable, "copy", that is equal to "game" in the form of a list
					copy[2*i] = letter #This takes the list "copy" and gives it an index of [2*i] before setting it = to "letter"
					game = "".join(copy) #This concatenates "game" with "copy"
			print(game) #This then prints "game"
		else: #This sets a procedure for if the conditional is false
			fails += 1 #This causes "fails" to be added to and then = to 1
			print("Incorrect!") #This prints "Incorrect!"
			print(6 - fails, "incorrect guesses remaining") #This prints 6 - the amount of fails, and then prints "incorrect guesses remaining" after
	if correct_guesses == code_letters: #This creates a conditional for if "correct_guesses" = "code_letters"
		print("You win!") #This prints "You win!"
		break #This causes a break in the code loop

if fails == 6: #This creates a conditional for if "fails" = 6
	print("You lose. The correct word was "+ word) #This prints "You lose. The correct word was " and then the word
        
#I refreshed my understanding and use of if, for, and while loops whilst building this code. I also refreshed my knowledge of lists, input, operators, ranges, and what can be done with lists.