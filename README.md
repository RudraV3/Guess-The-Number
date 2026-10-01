# Guess-The-Number
Guess the Number is a simple number-guessing game made in Python where the player attempts to guess a random number in a range within 10 attempts. 
There are lots of different features that is added into this program to make it more useful and gives the users a little more to do other than "guess the number" (although that is the whole point of the program...)

You can play the working game on [CodeHS](https://codehs.com/sandbox/rudravaja1/number-guessing-game/run) right now!
(Just click the blue hyperlink where it says "CodeHS")

Some of these features include:
- **Hints:** After each guess, the user immediately gets feedback, whether they got it right or *ABSOLUTELY* wrong.
- **Limited Guesses:** Each time you play the game, you are limited to only ten attempts, so if you suck at the game, you're not getting any more - deal with it.
- **Replay Prompt:** After you completed the game, you are asked if you want to play the game. If yes, then the program will restart, and if no, then the program will dismiss you.
- **No Nonsense:** If you accidentally mistyped or said some random gibberish for whatever reason in any of the prompts, then the program will reject that input, and will ask you to give it an actual *valid* answer.

# Logic of the Program 
The program introduces the random module so that it is able to generate random numbers that the game runs on. The entirety of the game is inside of a while True: loop, so the player can play for as long as they would like until they get prompted if they want to end the game and they say "no". 

To set the game's boundaries, there is a difficulty() function that helps with setting the range and intensity of the game. This prompts the user into inputing a difficulty that they want, whether it would be easy, medium, or hard. This changes the range of the numbers that they will guess from. Easy will be in a range from 1 to 1,000, medium will be within 1 to 5,000, and hard will be within 1 to 10,000.

The program also uses if/elif/else blocks in order to give out certain actions whenever the user does something. For example, if a user inputs a number, it will check if the number is greater than the correct number with the "if" block, and then will check if the number is less than the correct number with the "elif" block, and the rest of the numbers, which are numbers less than the correct number, will be detected using the "else" block.

There also exists a limited number of attempts to guess the number correctly, and if the number isn't correctly guessed before the number of attempts run out, the game will tell you that you lost, followed by a prompt that says if you want to play again. To keep track of the attempts, a while tries > 0 function is implemented, which determines whether or not the user ran out of attempts or not. After each guess, the program will subtract 1 from the number of tries, indicating that you have guessed. If the user has guessed the number correctly, then a "break" statement is used to exit the guessing loop immediately.

If the number of tries hits 0, then the program detects that the variable hit 0, which stops the game and tells the user that they lost. They are also prompted if they want to play again. If they say yes, then a continue statement runs, skipping the rest of the code and restarting the program. If they say no, then the program will print a goodbye message, and will stop. 

# Encountered Bugs
During my time coding this program, I have encountered many different bugs. If I had to be honest, the hardest part was fixing those bugs, because some of those bugs turned into millions of tiny bugs, and those were mildly frustrating to fix. Here are all of the bugs that I have taken note of. It isn't much, but those *really* started to give me a headache.

- **Value Error:** This was one of the first bugs I had encountered. I felt like I was finished with my program, and was just about to give it that final test. My functions looked good, there were no typos (I made SURE of it), and I have pretty much done everything correctly, or so I thought... My program asked me for the difficulty, and I accidentally added an extra "y" to the word. Next thing you know, the entire program crashed. I have spent many hours trying to find a cause, if there was even a fix or a way to ask the user to try again. Then, when I was doing my AP CSP course, I found my solution: the try/except blocks which would solve my issue.
- **Capitalization:** After that frustrating bug, I tested it numerous times to make sure that in every scenario, my program will work. One of the scenarios that *didn't* work was whenever I capitalized ANY letters in my word. I didn't know what to do, and I didn't just want to do the whole AP CSP course to find out, so I searched it up. There it was, the .strip() and .lower(), which will not only work for any capitalizaion, but also for any typos with special characters.
- **Infinite Guesses:** After I confimed everything worked, I decided to just have a little fun for myself, so I played it. I chose the hard difficulty, because I am the type of person who would take a challange (unless in public, then I can't). Then, guess after guess, I got them all wrong. As soon as I put in my final guess, it said that I had 0 tries, and to guess another number. It was weird, because if your number of attempts is 0, then you should've lost, but apparently my program thought otherwise. I had somehow completely overlooked that while I had my tries variable, I had actually never done anything with it. I quickly change the code so that with each attempt, the tries variable will go down in value by 1, which makes it so that whenever the tries hit 0 or lower, the program won't hallucinate and say that I have -218 tries left.

# Program Additional Info
**Programming Language:** Python 3
**License:** MIT (see LICENSE.txt for more information)
**Developer:** Rudra Vaja
