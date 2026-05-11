# Please write a program which asks the user which editor they are using. The program should 
# keep on asking until the user types in Visual Studio Code.

# Have a look at the example of expected behaviour below:

# Sample output
# Editor: Emacs
# not good
# Editor: Vim
# not good
# Editor: Word
# awful
# Editor: Atom
# not good
# Editor: Visual Studio Code
# an excellent choice!

# If the user types in Word or Notepad, the program counters with awful. Other unacceptable 
# editor choices receive the reply not good.

# The program should be case-insensitive in its reactions. That is, the same user input in 
# lowercase, uppercase or mixed case should trigger the same reaction:

## Solution:


input_string = input("Editor:")

while True :
    if input_string.lower() == 'visual studio code':
        print("an excellent choice!")
        break
    elif input_string.lower() == 'word':
        print("awful")
    else :
        print("not good")
    input_string = input("Editor:")