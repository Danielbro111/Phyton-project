import random ##This import is used to generate random numbers in python.Prety Interesting!

def printIntro():  ##Wow something new already!No need for {} in python only ":" so It seems
    print("""Hello and welcome!
This is my first time coding in Python!, Im excited to learn more.
I will be using this repo to store my projects and learn along the way. 
I hope you enjoy my mini games! :)  
I will be updating this repository as I learn and improve my coding skills.

          
Another thing I will be doing is leaving personal comments as I go!
""") ##Something Im use to is string templates, glad to see you can use them in python as well lol 



##It requires you to indent the code to make it work.Something which i havent seen personally in Java and kotlin
##Another thing! To make a comment you use "#" instead of "//" like in Java and Kotlin

def miniGame1(): 
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
     

def Choice(option):
    switcher = { ##Switch statement looks funny lol 
        1: lambda: miniGame1(), ##You need a comma, you dont need this in Java or Kotlin I believe 
        2: lambda: print("This game hasn't been made yet! Come back in a few days!")

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
    print("2: Print a message")
    try:
        option = int(input("Enter an option (1-2): "))
        Choice(option)
        print()
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__": ##Very new to me, You must used as an entry point to the program
       main() 