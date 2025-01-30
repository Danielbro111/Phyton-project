import random ##This import is used to generate random numbers in python.Prety Interesting!

def printIntro():  ##Wow something new already!No need for {} in python only ":" so It seems
    print("""Hello and welcome!
This is my first time coding in Python!, Im excited to learn more.
I will be using this repo to store my projects and learn along the way. 
I hope you enjoy my mini games! :)  
I will be updating this repository as I learn and improve my coding skills.

          
Another thing I will be doing is leaving personal comments as I go :)
""") ##Something Im use to is string templates, glad to see you can use them in python as well lol 



##It requires you to indent the code to make it work.Something which i havent seen personally in Java and kotlin
##Another thing! To make a comment you use "#" instead of "//" like in Java and Kotlin

def miniGame1(): 
    print()
    print("Welcome to the first mini game!") 
    print()
    print("In this game you will have to guess a number between 1 and 5.")
    print()
    print("Good luck!")
    numberToGuess = random.randint(1, 5)

    while True:
     try:
          guess = int(input("Enter a number between 1 and 5: "))
          if guess < 1 or guess > 5:
            print("Please enter a number between 1 and 5.")
          elif guess > numberToGuess:
            print("Too high!, please try again :) ")
          elif guess < numberToGuess:
            print("Too low!, please try again :) ")
          else:
            print("Congratulations! You guessed the number correctly!")
            break   ##Similar to java  use the break to end a loop
     except ValueError:
        print("Invalid input. Please enter a number.")
     

def miniGame2():
    words = ["python", "java", "javascript", "kotlin", "react", "angular"]
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    hangman_pics = ['''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
         ===''']

    print("""Welcome to Hangman!
The aim of the game is to guess the selected word (hint: it's a programming language) by guessing one letter at a time.
You have 6 wrong guesses allowed.
    """)
    
    while wrong_guesses < 6:
        print(hangman_pics[wrong_guesses])
        
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display +="_"
        print(f"\nWord: {display}") ##f is used to create a string literal something new to me
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        if "_" not in display:
            print(f"\nCongratulations! You won! The word was '{word}'!")
            break
            
       
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1:  ##this is a good way to check the length of a string
            print("Please enter just one letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)##append is used to add to a list in python
        
        if guess not in word:
            wrong_guesses += 1
            print(f"Wrong guess! {6 - wrong_guesses} guesses remaining.")
        else:
            print("Correct guess!")
    
    if wrong_guesses == 6:
        print(hangman_pics[6])
        print(f"\nGame Over! The word was '{word}'")


def Choice(option):
    switcher = { ##Switch statement looks funny lol 
        1: lambda: miniGame1(), ##You need a comma, you dont need this in Java or Kotlin I believe 
        2: lambda: miniGame2() 

    }
    func = switcher.get(option)
    if func:
        func()  ##This is different, You must call the function after the switch statement
    else:
        print("Invalid option. Please enter a number between 1 and 2.")



def main():
    printIntro()
    
    print("Please choose an option:")
    print("1: Play MiniGame 1")
    print("2: Play MiniGame 2")
    try:
        option = int(input("Enter an option (1-2): "))
        Choice(option)
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__": ##Very new to me, You must used as an entry point to the program
       main() 